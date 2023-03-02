import tenseal as ts
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import pickle
import random

# 密码学算法工具库，包含同态加密算法、AES对称加密算法、RSA非对称加密算法、椭圆曲线算法、生成密钥对、加密、解密、签名、验证等功能
# Google注释风格


class CipherBox:
    def __init__(self) -> None:
        pass

    def GenerateContext(self):
        """函数功能
        生成同态加密上下文

        Args:
            无

        Returns:
            context: 同态加密上下文
        """
        return ts.context(ts.SCHEME_TYPE.BFV, poly_modulus_degree=4096, plain_modulus=1032193)

    def GenerateSymmetricKey(self):
        """函数功能
        生成AES对称加密密钥

        Args:
            无

        Returns:
            AES.new(self.GenerateRandomKey(), AES.MODE_ECB): AES对称加密密钥
        """
        return AES.new(self.GenerateRandomKey(), AES.MODE_ECB)

    # 生成同态加密密钥
    def GenerateHEKey(self, context):
        """函数功能
        生成同态加密密钥

        Args:
            context: 同态加密上下文

        Returns:
            context.keygen(): 同态加密密钥
        """
        return context.keygen()

    # 生成RSA非对称加密密钥对
    def GenerateRSAKey(self):
        """函数功能
        生成RSA非对称加密密钥对

        Args:
            无

        Returns:
            RSA.generate(2048): RSA非对称加密密钥对
        """
        return RSA.generate(2048)

    # 生成AES随机密钥
    def GenerateRandomKey(self):
        """函数功能
        生成AES随机密钥

        Args:
            无

        Returns:
            bytes(random.randint(0, 255) for i in range(16)): AES随机密钥
        """
        return bytes(random.randint(0, 255) for i in range(16))

    # 生成随机数
    def GenerateRandomNumber(self):
        """
        生成随机数
        """
        pass

    # 生成DES随机密钥
    def GenerateDESKey(self):
        """函数功能
        生成DES随机密钥

        Args:
            无

        Returns:
            bytes(random.randint(0, 255) for i in range(8)): DES随机密钥
        """
        return bytes(random.randint(0, 255) for i in range(8))

    # 使用RSA非对称加密算法加密
    def RSAEncrypt(self, key, data):
        """函数功能
        使用RSA非对称加密算法加密

        Args:
            key: RSA非对称加密密钥对
            data: 待加密数据

        Returns:
            key.encrypt(data): 加密后的数据
        """
        return key.encrypt(data)

    # 使用RSA非对称加密算法解密
    def RSADecrypt(self, key, data):
        """函数功能
        使用RSA非对称加密算法解密

        Args:
            key: RSA非对称加密密钥对
            data: 待解密数据

        Returns:
            key.decrypt(data): 解密后的数据
        """
        return key.decrypt(data)

    # 使用椭圆曲线算法生成密钥对
    def GenerateECKey(self):
        """函数功能
        使用椭圆曲线算法生成密钥对

        Args:
            无

        Returns:
            key: 椭圆曲线算法密钥对
        """
        pass

    # 使用椭圆曲线算法签名
    def ECSign(self, key, data):
        """函数功能
        使用椭圆曲线算法签名

        Args:
            key: 椭圆曲线算法密钥对
            data: 待签名数据

        Returns:
            key.sign(data): 签名后的数据
        """
        pass

    # 使用椭圆曲线算法验证签名
    def ECVerify(self, key, data, signature):
        """
        使用椭圆曲线算法验证签名
        """
        pass

    # 使用AES对称加密算法加密

    def AESEncrypt(self, key, data):
        """函数功能
        使用AES对称加密算法加密

        Args:
            key: AES对称加密密钥
            data: 待加密数据

        Returns:
            encrypt(pad(data, AES.block_size)): 加密后的数据
        """
        aes = AES.new(key, AES.MODE_ECB)
        return aes.encrypt(pad(pickle.dumps(data), AES.block_size))

    # 使用AES对称加密算法解密
    def AESDecrypt(self, key, data):
        """函数功能
        使用AES对称加密算法解密

        Args:
            key: AES对称加密密钥
            data: 待解密数据

            Returns:
                unpad(key.decrypt(data), AES.block_size): 解密后的数据
                """
        aes = AES.new(key, AES.MODE_ECB)
        return pickle.loads(unpad(aes.decrypt(data), AES.block_size))

    # 使用DES对称加密算法加密
    def DESEncrypt(self, key, data):
        """函数功能
        使用DES对称加密算法加密

        Args:
            key: DES对称加密密钥
            data: 待加密数据

        Returns:
            key.encrypt(pad(data, DES.block_size)): 加密后的数据
        """
        return key.encrypt(pad(data, DES.block_size))

    # 使用DES对称加密算法解密
    def DESDecrypt(self, key, data):
        """函数功能
        使用DES对称加密算法解密

        Args:
            key: DES对称加密密钥
            data: 待解密数据

        Returns:
            unpad(key.decrypt(data), DES.block_size): 解密后的数据
        """
        return unpad(key.decrypt(data), DES.block_size)

    # 使用同态加密算法加密
    def HEEncrypt(self, context, data):
        """函数功能
        使用同态加密算法加密

        Args:
            context: 同态加密上下文
            data: 待加密数据

        Returns:
            encrypt( data): 加密后的数据
        """
        return ts.bfv_vector(context, data)

    # 使用同态加密算法解密
    def HEDecrypt(self, context, data):
        """函数功能
        使用同态加密算法解密

        Args:
            context: 同态加密上下文
            data: 待解密数据

        Returns:
            decrypt(data): 解密后的数据
        """
        return data.decrypt()

    # 使用CKKS同态加密算法加密
    def CKKSEncrypt(self, context, key, data):
        """函数功能
        使用CKKS同态加密算法加密

        Args:
            context: 同态加密上下文
            key: 同态加密密钥
            data: 待加密数据

        Returns:
            context.encrypt(key, data): 加密后的数据
        """
        pass

    # 使用CKKS同态加密算法解密
    def CKKSDecrypt(self, context, key, data):
        """函数功能
        使用CKKS同态加密算法解密

        Args:
            context: 同态加密上下文
            key: 同态加密密钥
            data: 待解密数据

        Returns:
            context.decrypt(key, data): 解密后的数据
        """
        pass


CipherBox = CipherBox()
# 演示RSA加解密
key = CipherBox.GenerateRSAKey()
print("RSA公钥:", RSA.import_key(key.publickey().export_key()).export_key())
print("RSA私钥:", RSA.import_key(key.export_key()).export_key())
# 演示AES加解密
key = CipherBox.GenerateRandomKey()
print("AES密钥:", key)
data = b'Hello World!'
print('原始数据：', data)
encrypted_data = CipherBox.AESEncrypt(key, data)
print('加密后数据：', encrypted_data)
decrypted_data = CipherBox.AESDecrypt(key, encrypted_data)
print('解密后数据：', decrypted_data)

# 演示同态加解密
context = CipherBox.GenerateContext()
data1 = [10]
data2 = [20]
print('原始数据1:', data1)
print('原始数据2:', data2)
encrypted_data1 = CipherBox.HEEncrypt(context, data1)
encrypted_data2 = CipherBox.HEEncrypt(context, data2)
encrypted_data3 = encrypted_data1+encrypted_data2
decrypted_data = CipherBox.HEDecrypt(context, encrypted_data3)
print('解密后数据：', decrypted_data)
