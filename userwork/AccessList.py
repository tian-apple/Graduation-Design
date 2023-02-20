# 访问控制列表
# User3-User10构造数据上传结构体，分别包含加密字符字段，加密数值字段以及一个访问控制列表
# e.g. User3如果允许User10访问自己的加密数据，则使用User10的公钥加密自己的对称加密密钥以及同态解密密钥，
# 并将（User10标识，加密后的密钥）放置于访问控制列表中。

import SimpleUser

# 访问控制列表单个元素格式为[数据拥有者的用户标识，授权给用户的用户标识]


class AccessControlList:
    list = []

    def __init__(self) -> None:
        pass

    def add(self, user1, user2):
        self.list.append([user1.userid, user2.userid])

    def findowner(self, id):
        for i in self.list:
            if i[1] == id:
                return i[0]
        return None
