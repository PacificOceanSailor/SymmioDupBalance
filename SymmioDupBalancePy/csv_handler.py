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