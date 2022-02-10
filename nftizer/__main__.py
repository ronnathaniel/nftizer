
from nftizer.compiler import CompiledContract
from nftizer.build_contract import build, options_default
from nftizer.w3 import get_w3


def run():
    w3 = get_w3()
    build(options_default())
    with open('SAMOContract.sol', 'r') as fh:
        source = fh.read()
        # print(source)
    contract = CompiledContract(source, w3)

    # contract_build = w3.eth.contract(abi=contract_comp.abi, bytecode=contract_comp.bytecode)
    # print(contract_build)

    tx_hash = contract.w3build.constructor().transact()
    print(tx_hash)

    tx_reciept = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(tx_reciept)

    contract_deployed = w3.eth.contract(address=tx_reciept.contractAddress, abi=contract.abi)
    print(contract_deployed)


if __name__ == '__main__':
    run()