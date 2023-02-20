# User2将数据上传结构体上链存储。（模拟通过web服务器进行数据上传）
from web3 import Web3, HTTPProvider
import os
import json


class DataControl:
    w3 = ""
    filepath = ""
    data = ""  # 合约abi
    contract_address = ""  # 合约地址
    contract = ""  # 合约对象

    def __init__(self):  # 初始化,连接合约
        self.w3 = Web3(HTTPProvider(
            "http://localhost:8900", request_kwargs={'timeout': 120}))
        self.filepath = 'build/contracts/Working.json'
        with open(self.filepath, encoding='utf-8') as json_file:
            self.data = json.load(json_file)
        self.contract_address = '0x06c58dAc845A0888979F222e81d13D8Db9FA26E8'
        self.contract = self.w3.eth.contract(
            address=self.contract_address, abi=self.data['abi'])

    def upload(self, name, priceandnmuber, id, keys):
        print("标记")
        self.contract.functions.set(name, priceandnmuber, id, keys).transact(
            {'from': self.w3.eth.accounts[1],
             'gas': 10000000000}
        )
        print("上传成功")

    def Download(self, userid):
        (name, priceandnumber, id, keys) = self.contract.functions.getdata(userid).call()
        return (name, priceandnumber, keys)

    def Getcount(self):
        return self.contract.functions.getcount().call()

    def RandomDownload(self, count):
        (name, priceandnumber, id,
         keys) = self.contract.functions.getrandomdata(count).call()
        return (name, priceandnumber, id, keys)
