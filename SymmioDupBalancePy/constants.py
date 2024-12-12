import json

csv_filename = "symmioDupBalances.csv"
csv_column_names = ["address", "balanceOf()", "allocatedBalanceOfPartyA()", "total"]

fantom_subgraph_url = "https://api.studio.thegraph.com/query/97235/symmdupbalancefantom/version/latest"
fantom_w3_rpc = "https://rpcapi.fantom.network"
fantom_symmio_contract_address = "0x762407bEd807184F90F3eDcF2D7Ac9CB9d8901c6"

collatral_min = 10**18

with open('symmio_balance_abi.json', 'r') as file:
    symmio_balance_abi = json.load(file)
