# User3-User10本地使用对称加密密钥加密字符型交易数据（如商品名称），使用同态加密私钥加密数值型交易数据（如商品价格与数量）。
# User3-User10构造数据上传结构体，分别包含加密字符字段，加密数值字段以及一个访问控制列表 e.g. User3如果允许User10访问自己的加密数据，
# 则使用User10的公钥加密[自己的对称加密密钥,同态解密密钥]，并将（User10标识，加密后的密钥）放置于访问控制列表中。

import DataTransform
import KeyCenter
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import pickle
import tenseal as ts
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
from Crypto.PublicKey import RSA
import random
import time


class user:
    userid = ""
    SymmetricKey = ""  # 对称加密密钥
    context = ""  # 同态加密上下文，封装公钥和私钥
    HEpublickey = ""  # 同态加密公钥
    HEsecretkey = ""  # 同态加密私钥
    RSApublickey = ""  # 非对称加密公钥
    RSAsecretkey = ""  # 非对称加密私钥
    CommidityName = ""  # 商品名称,字符型
    EncryptCommidityName = ""  # 对称加密后的商品名称,bytes型
    CommidityPrice = 0  # 商品价格,数值型
    CommidityNumber = 0  # 商品数量,数值型
    CommidityBalance = 0  # 余额
    CommidityPriceandNumber = b''  # 同态加密的价格和数量序列
    keys = b''  # 存放自己用对方公钥加密的对称加密密钥和同态解密密钥
    isEncrypt = False
    dataserver = DataTransform.DataControl()

    def __init__(self, name, price, number) -> None:
        self.CommidityName = name
        self.CommidityPrice = price
        self.CommidityNumber = number
        self.CommidityBalance = random.randint(100, 1000)

    def encrypt(self):  # 加密自己的交易数据
        if(self.SymmetricKey == ""):
            print("请先联系权威机构获取密钥")
            return
        elif self.isEncrypt == True:
            print("数据已加密,请勿重复加密")
            return
        else:
            self.EncryptCommidityName = pickle.dumps(self.CommidityName)
            aes = AES.new(self.SymmetricKey, AES.MODE_ECB)
            self.EncryptCommidityName = aes.encrypt(
                pad(self.EncryptCommidityName, AES.block_size))  # 对称加密商品名称

            self.CommidityPriceandNumber = [
                self.CommidityPrice, self.CommidityNumber]
            self.CommidityPriceandNumber = ts.bfv_vector(
                self.context, self.CommidityPriceandNumber).serialize()   # 同态加密商品价格和数量并序列化
            self.isEncrypt = True

    def GetControl(self, user, AccessControlList):  # 默认允许访问自己的加密数据，添加控制列表,并将数据上链
        print("用户"+self.userid+"授权用户"+user.userid+"访问自己的数据")
        if(self.SymmetricKey == ""):
            print("请先联系权威机构获取密钥")
            return
        else:  # 加密自己的对称加密密钥和同态解密密钥，用对方的公钥加密
            cipher = PKCS1_cipher.new(user.RSApublickey)
            # 由于同态私钥太长，所以需要分段加密
            rsa_text = []
            for i in range(0, len(self.HEsecretkey), 245):
                cont = self.HEsecretkey[i:i+245]
                rsa_text.append(cipher.encrypt(cont))
            cipher_text = b''.join(rsa_text)
            self.keys = pickle.dumps([cipher.encrypt(
                self.SymmetricKey), cipher_text])
            print(self.userid+"的数据加密成功")
            AccessControlList.add(self, user)  # 添加控制列表
            self.dataserver.upload(
                self.EncryptCommidityName, self.CommidityPriceandNumber, user.userid, self.keys)  # 数据上链

    def DownloadData(self):
        print(self.userid+"从链上下载数据")
        (username, userpriceandnumber, userkeys) = self.dataserver.Download(
            self.userid)  # 从链中下载授权给自己的数据，包括对方的对称加密密钥，同态私钥，加密数据
        userkeys = pickle.loads(userkeys)  # 解序列化,变成[加密对称密钥，加密同态私钥]
        cipher = PKCS1_cipher.new(self.RSAsecretkey)
        # 由于同态私钥太长，所以需要分段解密
        rsa_text = []
        for i in range(0, len(userkeys[1]), 256):
            cont = userkeys[1][i:i+256]
            rsa_text.append(cipher.decrypt(cont, 0))
        userHEsecretkey = b''.join(rsa_text)  # 同态私钥
        userSymmetricKey = cipher.decrypt(userkeys[0], 0)  # 对称加密密钥
        # 解密商品名称("字符型数据")
        aes = AES.new(userSymmetricKey, AES.MODE_ECB)
        userCommidityName = aes.decrypt(username)
        userCommidityName = pickle.loads(
            unpad(userCommidityName, AES.block_size))
        # 解密商品价格和数量("数值型数据")
        usercontext = ts.context_from(userHEsecretkey)
        userCommidityPriceandNumber = ts.bfv_vector_from(
            usercontext, userpriceandnumber)
        userCommidityPriceandNumber = userCommidityPriceandNumber.decrypt()
        userprice = userCommidityPriceandNumber[0]
        usernumber = userCommidityPriceandNumber[1]
        print("商品名称:", userCommidityName)
        print("商品价格:", userprice)
        print("商品数量:", usernumber)

    def DownloadRamdomData(self, keycenter, index: int, AccessControlList):
        print(self.userid, "发起密文验证请求,调用地址为",
              self.dataserver.contract_address, "合约")
        i = random.randint(0, len(AccessControlList.list)-1)
        start = time.time()
        (username, userpriceandnumber, id,
         userkeys) = self.dataserver.RandomDownload(i)
        ownerid = AccessControlList.findowner(id)
        print("获取到区块链中第"+str(i)+"条数据，为"+str(ownerid)+"授权给"+str(id)+"的数据")
        data = keycenter.verify(
            userpriceandnumber, ownerid, index, self.CommidityBalance)
        print("最终结果为"+str(data)+",检定值为"+str(index))
        if data >= index:
            print("密文验证成功")
        else:
            print("密文验证失败")
        end = time.time()
        print("密文验证耗时:", (end-start)*1000, "ms")
