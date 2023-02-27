import SimpleUser
import KeyCenter
import AccessList
import tenseal as ts

# 变量初始化
key = KeyCenter.KeyManagerCenter()
user1 = SimpleUser.user("user1_Xiaomi", 59, 32)
user2 = SimpleUser.user("usser2_Apple", 23, 45)
user3 = SimpleUser.user("user3_Lenovo", 53, 79)
user4 = SimpleUser.user("user4_Google", 83, 45)
user5 = SimpleUser.user("user5_ByteDance", 69, 45)
user10 = SimpleUser.user("user10_Huawei", 24, 30)
controllist = AccessList.AccessControlList()


# 1.密钥生成
# 首先，User1（权威机构）为系统中的每个用户生成独立的公钥与私钥，对称加密密钥以及全局同态加密公钥与私钥并进行存储。
print("**********************密钥生成**********************")
key.register(user1)
key.register(user2)
key.register(user3)
key.register(user4)
key.register(user5)
key.register(user10)
print("*********************展示角色信息**********************")
print("userid", user3.userid)
print("RSApublickey", user3.RSApublickey)
print("RSAsecretkey", user3.RSAsecretkey)
print("Symmetrickey", user3.SymmetricKey)
print("HEpublickey", user3.context.public_key())
print("HEsecretkey", user3.context.secret_key())
# print(user10.userid)
# print(user10.SymmetricKey)
# print(user10.HEpublickey)
# print(user10.HEsecretkey)

# 2.数据加密
# User3-User10本地使用对称加密密钥加密字符型交易数据（如商品名称），使用同态加密私钥加密数值型交易数据（如商品价格与数量）。
print("**********************数据加密**********************")
user1.encrypt()
user2.encrypt()
user3.encrypt()
user4.encrypt()
user5.encrypt()
user10.encrypt()
print("字符密文", user3.EncryptCommidityName)
print("数值密文", user3.CommidityPriceandNumber[0:32])

# 3.访问控制
# User3-User10构造数据上传结构体，分别包含加密字符字段，加密数值字段以及一个访问控制列表
# e.g. User3如果允许User10访问自己的加密数据，则使用User10的公钥加密[自己的对称加密密钥,同态解密密钥]，
# 并将（User10标识，加密后的密钥）放置于访问控制列表中
print("**********************访问控制**********************")
user3.GetControl(user10, controllist)
user1.GetControl(user2, controllist)
user5.GetControl(user4, controllist)
user10.GetControl(user1, controllist)

# 4.数据获取
# User10检查新上链数据的访问控制列表，发现自己的标识后，下载对应数据，并使用私钥解密访问控制列表中的加密密钥，进而解密数据。
print("**********************数据获取**********************")
user10.DownloadData()
user4.DownloadData()

# 5.数据验证
print("**********************数据验证**********************")
user1.DownloadRamdomData(key, 3000, controllist)
