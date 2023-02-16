import pickle
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
from Crypto.PublicKey import RSA

a = "1234567890"
for i in range(0, len(a), 2):
    print(a[i:i+2])
    print(" ")
