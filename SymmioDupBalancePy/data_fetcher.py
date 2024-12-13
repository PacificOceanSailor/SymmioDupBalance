import json

from web3.exceptions import Web3Exception
from web3 import Web3
import constants as const
import requests


class DataFetcher:
    def __init__(self,
                 w3_url,
                 graph_api_url,
                 symmio_contract_address,
                 symmio_contract_abi,
                 deus_multi_address,
                 deus_multi_abi
                 ):
        self.w3 = Web3(Web3.HTTPProvider(w3_url))
        self.api_url = graph_api_url
        self.symmio_diamond = self.w3.eth.contract(
            address=symmio_contract_address,
            abi=symmio_contract_abi
        )
        self.deus_multi_account = self.w3.eth.contract(
            address=deus_multi_address,
            abi=deus_multi_abi
        )

    def getBalances(self, address: str) -> (int, int):
        balance = self.symmio_diamond.functions.balanceOf(address).call()
        allocatedBalancePA = self.symmio_diamond.functions.allocatedBalanceOfPartyA(address).call()
        return balance, allocatedBalancePA

    def getOwner(self, address):
        try:
            return self.deus_multi_account.functions.owner(address).call()
        except Web3Exception:
            return self.deus_multi_account.functions.owners(address).call()

    def querySymmioDupAddresses(self):
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
            response = requests.post(self.api_url, headers=headers, data=json.dumps(payload))
            if response.status_code == 200:
                data = response.json()
                users = [Web3.to_checksum_address(deposit['user']) for deposit in data['data']['deposits']]
                if not (len(users) > 0):
                    break
                all_users += users
            else:
                raise Exception(f"Query failed with status code {response.status_code}: {response.text}")
            _skip += _skip_step
        return list(set(all_users))
