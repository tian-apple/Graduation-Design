# User1是系统监管者以及密钥管理中心
# User1（权威机构）为系统中的每个用户生成独立的公钥与私钥，对称加密密钥以及全局同态加密公钥与私钥并进行存储。

import random
import uuid
import pickle
import tenseal as ts
from Crypto.PublicKey import RSA


class KeyManagerCenter:
    keylist = []

    def __init__(self) -> None:
        pass

    def register(self, user):
        if(user.userid != ""):
            print("已经分发过密钥，无需重复分发")
            return
        else:
            user.userid = str(uuid.uuid4().hex.upper()[0:6])  # 生成用户标识
            tempstr = str(uuid.uuid4().hex.upper()[0:16])
            key_pair = RSA.generate(2048)  # 生成RSA密钥对
            user.SymmetricKey = bytes(tempstr.encode('utf-8'))  # 生成对称加密密钥
            context = ts.context(
                ts.SCHEME_TYPE.BFV, poly_modulus_degree=4096, plain_modulus=1032193)
            user.context = context
            user.HEpublickey = context.serialize(
                save_public_key=True, save_galois_keys=False, save_relin_keys=False, save_secret_key=False)

            user.HEsecretkey = context.serialize(
                save_secret_key=True, save_galois_keys=False, save_relin_keys=False, save_public_key=False)

            user.RSApublickey = RSA.import_key(
                key_pair.publickey().export_key())
            user.RSAsecretkey = RSA.import_key(key_pair.export_key())
            self.keylist.append([user.userid, user.RSApublickey, user.RSAsecretkey, user.SymmetricKey,
                                 user.HEpublickey, user.HEsecretkey])

    def verify(self, priceandnumber, id, index):
        for i in self.keylist:
            if(i[0] == id):
                usercontext = ts.context_from(i[5])
                priceandnumber = ts.bfv_vector_from(
                    usercontext, priceandnumber)
                priceandnumber = priceandnumber.decrypt()
                price = priceandnumber[0]
                number = priceandnumber[1]
                return price*number
        return False
