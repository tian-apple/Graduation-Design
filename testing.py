from Pyfhel import Pyfhel, PyCtxt

# 初始化Pyfhel加密对象
HE = Pyfhel()
HE.contextGen(p=65537, m=4096, base=2, intDigits=64)

# 生成公钥和私钥
HE.keyGen()

# 加密两个整数
a = 42
b = 13
ctxt_a = HE.encryptInt(a)
ctxt_b = HE.encryptInt(b)

# 加法运算
ctxt_sum = ctxt_a + ctxt_b
# 解密得到结果
result_sum = HE.decryptInt(ctxt_sum)
print("加法结果：", result_sum)

# 乘法运算
ctxt_prod = ctxt_a * ctxt_b
# 解密得到结果
result_prod = HE.decryptInt(ctxt_prod)
print("乘法结果：", result_prod)
