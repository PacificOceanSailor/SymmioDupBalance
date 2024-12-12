from web3 import Web3


class BalanceFetcher:
    def __init__(self, url, contract_address, contract_abi):
        self.w3 = Web3(Web3.HTTPProvider(url))
        self.contract = self.w3.eth.contract(address=contract_address, abi=contract_abi)

    def getBalance(self, address: str) -> (int, int):
        balance = self.contract.functions.balanceOf(address).call()
        allocatedBalancePA = self.contract.functions.allocatedBalanceOfPartyA(address).call()
        return balance, allocatedBalancePA
