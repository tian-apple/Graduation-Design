import SimpleUser
import KeyCenter
import AccessList
import tenseal as ts

# 变量初始化
key = KeyCenter.KeyManagerCenter()
user3 = SimpleUser.user("user3_Lenovo", 53, 798)
user10 = SimpleUser.user("user10_Huawei", 24, 30)
controllist = AccessList.AccessControlList()


# 1.密钥生成
# 首先，User1（权威机构）为系统中的每个用户生成独立的公钥与私钥，对称加密密钥以及全局同态加密公钥与私钥并进行存储。
key.register(user3)
key.register(user10)
print("user3:")
print(user3.userid)
# print(user3.RSAsecretkey)
print(user3.SymmetricKey)
# print(user3.HEpublickey)
# print(user3.HEsecretkey)
print("user10:")
print(user10.userid)
print(user10.SymmetricKey)
# print(user10.HEpublickey)
# print(user10.HEsecretkey)

# 2.数据加密
# User3-User10本地使用对称加密密钥加密字符型交易数据（如商品名称），使用同态加密私钥加密数值型交易数据（如商品价格与数量）。
user3.encrypt()
user10.encrypt()

# 3.访问控制
# User3-User10构造数据上传结构体，分别包含加密字符字段，加密数值字段以及一个访问控制列表
# e.g. User3如果允许User10访问自己的加密数据，则使用User10的公钥加密[自己的对称加密密钥,同态解密密钥]，
# 并将（User10标识，加密后的密钥）放置于访问控制列表中
user3.GetControl(user10, controllist)
# print(controllist.list)
user10.DownloadData()
