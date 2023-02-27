
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import pickle
import tenseal as ts
from web3 import Web3, HTTPProvider


class binary:
    data = "my work"
    data1 = [2]
    data2 = [3]
    password = b'1234568987987639'

    def __init__(self, data):
        self.data = "my work"

    def __str__(self):
        return self.data

    # 先序列化后加密
    def storge(self):
        global list_data
        global password
        list_data = pickle.dumps(self.data)
        aes = AES.new(self.password, AES.MODE_ECB)
        list_data = aes.encrypt(pad(list_data, AES.block_size))
        print("加密后的数据为：", list_data)

    def unstorage(self):  # 先解密后反序列化
        global list_data
        global password
        aes = AES.new(self.password, AES.MODE_ECB)
        list_data = aes.decrypt(list_data)
        list_data = pickle.loads(unpad(list_data, AES.block_size))
        print("解密后的数据为：", list_data)

    def HEtest(self):
        context = ts.context(ts.SCHEME_TYPE.BFV,
                             poly_modulus_degree=4096, plain_modulus=1032193)
        context.has_public_key = True
        context.has_secret_key = True
        HEpublickey = context.serialize(
            save_public_key=True)
        HEsecretkey = context.serialize(
            save_secret_key=True)
        print("HEpublickey", HEpublickey[0:64])
        print("HEsecretkey", HEsecretkey[0:64])



binarydata = binary("my work")
binarydata.storge()
binarydata.unstorage()
binarydata.HEtest()

RPC = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
print(RPC.isConnected())
 