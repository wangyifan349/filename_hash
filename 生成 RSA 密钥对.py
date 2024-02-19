from Crypto.PublicKey import RSA

# 生成 RSA 密钥对
key = RSA.generate(4096)

# 获取私钥
private_key = key.export_key('PEM')

# 获取公钥
public_key = key.publickey().export_key('PEM')

# 将私钥保存到文件
with open('private_key.pem', 'wb') as f:
    f.write(private_key)

# 将公钥保存到文件
with open('public_key.pem', 'wb') as f:
    f.write(public_key)

print("RSA 密钥对已生成并保存到 private_key.pem 和 public_key.pem 文件中")
