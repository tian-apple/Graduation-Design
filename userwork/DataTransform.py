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
        self.contract_address = '0xC6378A2aC69CE394B4eb2fFbA2023e8D16e88589'
        self.contract = self.w3.eth.contract(
            address=self.contract_address, abi=self.data['abi'])
        self.contract.functions.cleanup().transact(
            {'from': self.w3.eth.accounts[1],
                'gas': 10000000000}
        )

    def upload(self, name, priceandnmuber, id, keys):  # 数据上链
        self.contract.functions.set(name, priceandnmuber, id, keys).transact(
            {'from': self.w3.eth.accounts[1],
             'gas': 10000000000}
        )
        print("授权给"+id+"的数据上传成功")
        # 展示交易信息
        print("交易信息：")
        print("交易账户：", self.w3.eth.accounts[1])
        print("交易金额：", self.w3.eth.getBalance(self.w3.eth.accounts[1]))
        print("交易次数：", self.w3.eth.getTransactionCount(
            self.w3.eth.accounts[1]))

    def Download(self, userid):
        (name, priceandnumber, id, keys) = self.contract.functions.getdata(userid).call()
        return (name, priceandnumber, keys)

    def Getcount(self):  # 获取链上结构体数组长度
        return self.contract.functions.count().call()

    def RandomDownload(self, count):  # 随机获取链上数据
        (name, priceandnumber, id,
         keys) = self.contract.functions.getrandomdata(count).call()
        return (name, priceandnumber, id, keys)

    def getall(self):  # 获取链上所有数据
        return self.contract.functions.getall().transact(
            {'from': self.w3.eth.accounts[1],
                'gas': 10000000000}
        )
