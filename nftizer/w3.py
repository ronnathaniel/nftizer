
import os
from web3 import Web3


w3 = None
infura_project_key = os.getenv('INFURA_PROJECT_KEY')


def get_w3():
    global w3
    if not w3:
        w3 = Web3(Web3.HTTPProvider("https://ropsten.infura.io/v3/" + infura_project_key))

    # w3.eth.default_account = w3.eth.accounts[0]
    print(w3.eth.accounts)
    return w3


