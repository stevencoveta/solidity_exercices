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
# calling isActive returns false beacause the action of setting the state has not been invoke yet

key="43f9b7cca7481abc3d7824c129a40217fc5dfa35110861ed9996d8c49ccfd96f"
acct = w3.eth.account.privateKeyToAccount(key)

nonce = w3.eth.getTransactionCount(acct.address)


tx = contract.functions.addPerson("goo","goll").buildTransaction({
    "from": acct.address,
    "nonce": nonce
})

sign_tx = acct.signTransaction(tx)

tx_hash = w3.eth.sendRawTransaction(sign_tx.rawTransaction)
print(tx_hash.hex())

tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

print("Receipt accepted. gasUsed={gasUsed} blockNumber={blockNumber}". format(**tx_receipt))

print(contract.functions.people(1).call())
print(contract.functions.peopleCount().call())
