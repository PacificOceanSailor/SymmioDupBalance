import ABIs
from web3 import Web3
csv_filename_fantom = "symmioDupBalancesFantom.csv"
csv_filename_base = "symmioDupBalancesBase.csv"
csv_column_names = ["sender_address", "MultiAccount:owner()", "balanceOf()", "allocatedBalanceOfPartyA()", "total"]

fantom_subgraph_url = "https://api.studio.thegraph.com/query/97235/symmdupbalancefantom/version/latest"
fantom_w3_rpc = "https://rpcapi.fantom.network"
fantom_symmio_contract_address = Web3.to_checksum_address("0x762407bEd807184F90F3eDcF2D7Ac9CB9d8901c6")
fantom_deusMultiAccount_contract_address = Web3.to_checksum_address("0x0937bC09b8D073E4F1abE85470969475f714Ca6c")
fantom_deusMultiAccount_contract_abi = ABIs.fantom_deus_multi_account

base_subgraph_url = "https://api.studio.thegraph.com/query/97235/symmdupbalancebase/version/latest"
base_w3_rpc = "https://mainnet.base.org"
base_symmio_contract_address = Web3.to_checksum_address("0x52e2230cdb80edebdadafcf24033608c9a636d7d")
base_deusMultiAccount_contract_address = Web3.to_checksum_address("0x724796d2e9143920B1b58651B04e1Ed201b8cC98")
base_deusMultiAccount_contract_abi = ABIs.base_deus_multi_account

collateral_min = 10 ** 18

symmio_balance_abi = ABIs.symmio_balance
