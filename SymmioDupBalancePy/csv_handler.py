import csv

import constants as const


def createSymmioDupBalancesCsv(addresses, dataFetcher, filename):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        total_balance = 0
        total_allocated_balance = 0
        total = 0
        writer.writerow(const.csv_column_names)
        balance: int
        allocatedBalance: int
        for address in addresses:
            balance, allocatedBalance = dataFetcher.getBalances(address)
            balanceTotal = balance+allocatedBalance
            if balanceTotal > const.collateral_min:
                total_balance += balance
                total_allocated_balance += allocatedBalance
                total += balanceTotal
                owner = dataFetcher.getOwner(address)
                writer.writerow([address, owner, balance, allocatedBalance, balanceTotal])
        writer.writerow(["SUM", None, total_balance, total_allocated_balance, total])