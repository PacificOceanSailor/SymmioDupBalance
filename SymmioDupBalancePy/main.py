import csv
import json

import requests
from web3 import Web3
import constants as const
from balance_fetcher import BalanceFetcher


def querySymmioDupAddresses(url):
    all_users = []
    _skip = 0
    _skip_step = 1000
    while True:
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "query": f"""
            {{
                deposits(first:{_skip_step}, skip:{_skip}){{
                    user
                }}
            }}
            """,
            "operationName": "Subgraphs",
            "variables": {}
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            data = response.json()
            users = [Web3.to_checksum_address(deposit['user']) for deposit in data['data']['deposits']]
            if not len(users) > 0:
                break
            all_users += users
        else:
            raise Exception(f"Query failed with status code {response.status_code}: {response.text}")
        _skip += _skip_step
    return list(set(all_users))


def createSymmioDupBalancesCsv(addresses, balanceFetcher, filename):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        total_balance = 0
        total_allocated_balance = 0
        total = 0
        writer.writerow(const.csv_column_names)
        balance: int
        allocatedBalance: int
        for address in addresses:
            balance, allocatedBalance = balanceFetcher.getBalance(address)
            balanceTotal = balance+allocatedBalance
            if balanceTotal > const.collatral_min:
                total_balance += balance
                total_allocated_balance += allocatedBalance
                total += balanceTotal
                writer.writerow([address, balance, allocatedBalance, balanceTotal])
        writer.writerow(["SUM", total_balance, total_allocated_balance, total])


def main():
    balanceFetcher = BalanceFetcher(
        const.fantom_w3_rpc,
        const.fantom_symmio_contract_address,
        const.symmio_balance_abi
    )

    addresses = querySymmioDupAddresses(const.fantom_subgraph_url)
    createSymmioDupBalancesCsv(addresses, balanceFetcher, const.csv_filename)
    print(f"checked {len(addresses)}")


if __name__ == "__main__":
    main()