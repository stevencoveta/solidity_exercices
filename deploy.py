from web3 import Web3
from solcx import install_solc
from solcx import compile_source
import json 
from solcx import compile_source, compile_files
import pandas as pd 
import json

# change compile for different contracts files
compiled_sol = compile_files(["./getting_started/TokenBuy.sol"])

contract_id, contract_interface  = compiled_sol.popitem()

# Local ganache blockchain
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

#Private local ganache key 
key="43f9b7cca7481abc3d7824c129a40217fc5dfa35110861ed9996d8c49ccfd96f"

acct = w3.eth.account.privateKeyToAccount(key)
abi = contract_interface['abi']

with open("./getting_started/abi.txt","w") as outfile: 
    json.dump(abi, outfile)


contract = w3.eth.contract(abi=abi, bytecode=contract_interface['bin'])


print(w3.eth.getTransactionCount(acct.address))


tx = contract.constructor().buildTransaction({
       "from": acct.address,
       "nonce": w3.eth.get_transaction_count(acct.address),
       "gasPrice": w3.toWei("1","gwei")
})

print("signing transaction")

sign_tx = acct.signTransaction(tx)

tx_hash = w3.eth.send_raw_transaction(sign_tx.rawTransaction)
print(tx_hash.hex())

tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

print("contract deployed at:", tx_receipt.contractAddress)


with open("./getting_started/deployed_contract_adress.txt","w") as outfile: 
    json.dump(tx_receipt.contractAddress, outfile)