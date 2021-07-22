from eth_utils import address
import pandas as pd 
from web3 import Web3
import json


w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

with open('./getting_started/abi.txt') as json_file:
    abi = json.load(json_file)

with open('./getting_started/deployed_contract_adress.txt') as json_file:
    contract_adr= json.load(json_file)

contract = w3.eth.contract(address = contract_adr, abi = abi  )

print(contract.functions.owner.call())
