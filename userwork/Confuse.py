from web3 import Web3, HTTPProvider
import os
import json

w3 = Web3(HTTPProvider("http://localhost:8900",
          request_kwargs={'timeout': 120}))
filepath = 'build/contracts/Confuse.json'
with open(filepath, encoding='utf-8') as json_file:
    data = json.load(json_file)
contract_address = '0xF91e31ABcef6DbB2236398FEc238F2f5DdF76eC6'
contract = w3.eth.contract(address=contract_address, abi=data['abi'])

# 开始混淆过程
res = contract.functions.update(18, 28).transact({'from': w3.eth.accounts[0]})
res = contract.functions.update(18, 28).call()
# res转化为int类型
print("更新了第", res[0], "条数据 ,同时混淆了第", res[1], res[2], res[3], res[4], "条数据")
