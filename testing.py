import pickle
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
from Crypto.PublicKey import RSA
import random
import uuid
import rsa

# 生成两对不同的密钥
(pubkey1, privkey1) = rsa.newkeys(512)
(pubkey2, privkey2) = rsa.newkeys(512)
# 打印公钥和私钥
print(pubkey1)
print(privkey1)
print(pubkey2)
print(privkey2)
print()