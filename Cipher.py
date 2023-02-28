import tenseal as ts
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import pickle
import random

# 密码学算法工具库，包含同态加密算法、AES对称加密算法、RSA非对称加密算法、椭圆曲线算法、生成密钥对、加密、解密、签名、验证等功能


class CipherBox:
    def __init__(self) -> None:
        pass

    def GenerateContext(self):
        """
        生成同态加密上下文
        """
        pass

    def GenerateSymmetricKey(self):
        """
        生成对称加密密钥
        """
        pass

    # 生成同态加密密钥
    def GenerateHEKey(self, context):
        """
        生成同态加密密钥
        """
        pass

    # 生成RSA非对称加密密钥对
    def GenerateRSAKey(self):
        """
        生成RSA非对称加密密钥对
        """
        pass

    # 生成AES随机密钥
    def GenerateRandomKey(self):
        """
        生成AES随机密钥
        """
        pass

    # 生成随机数
    def GenerateRandomNumber(self):
        """
        生成随机数
        """
        pass

    # 使用RSA非对称加密算法加密
    def RSAEncrypt(self, key, data):
        """
        使用RSA非对称加密算法加密
        """
        pass

    # 使用RSA非对称加密算法解密
    def RSADecrypt(self, key, data):
        """
        使用RSA非对称加密算法解密
        """
        pass

    # 使用AES对称加密算法加密
    def AESEncrypt(self, key, data):
        """
        使用AES对称加密算法加密
        """
        pass

    # 使用AES对称加密算法解密
    def AESDecrypt(self, key, data):
        """
        使用AES对称加密算法解密
        """
        pass

    # 使用同态加密算法加密
    def HEEncrypt(self, context, key, data):
        """
        使用同态加密算法加密
        """
        pass

    # 使用同态加密算法解密
    def HEDecrypt(self, context, key, data):
        """
        使用同态加密算法解密
        """
        pass

    # 使用同态加密算法加密
    def CKKSEncrypt(self, context, key, data):
        """
        使用同态加密算法加密
        """
        pass
