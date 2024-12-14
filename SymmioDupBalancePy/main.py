import constants as const
from csv_handler import createSymmioDupBalancesCsv
from data_fetcher import DataFetcher


def main():
    dataFetcher = DataFetcher(
        const.fantom_w3_rpc,
        const.fantom_subgraph_url,
        const.fantom_symmio_contract_address,
        const.symmio_balance_abi,
        const.fantom_deusMultiAccount_contract_address,
        const.fantom_deusMultiAccount_contract_abi
    )
    addresses = dataFetcher.querySymmioDupAddresses()
    createSymmioDupBalancesCsv(addresses, dataFetcher, const.csv_filename_fantom)
    print(f"checked {len(addresses)} unique addresses on fantom")

    # dataFetcher = DataFetcher(
    #     const.base_w3_rpc,
    #     const.base_subgraph_url,
    #     const.base_symmio_contract_address,
    #     const.symmio_balance_abi,
    #     const.base_deusMultiAccount_contract_address,
    #     const.base_deusMultiAccount_contract_abi
    # )
    # addresses = dataFetcher.querySymmioDupAddresses()
    # createSymmioDupBalancesCsv(addresses, dataFetcher, const.csv_filename_base)
    # print(f"checked {len(addresses)} unique addresses on base")


if __name__ == "__main__":
    main()
