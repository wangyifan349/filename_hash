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





import gnupg

# 初始化GnuPG对象
gpg = gnupg.GPG()#需要安装GnuPG

# 生成 PGP 密钥对
input_data = gpg.gen_key_input(key_type="RSA", key_length=2048)
key = gpg.gen_key(input_data)

# 保存私钥到文件
private_key = gpg.export_keys(key.fingerprint)
with open('private_key.asc', 'w') as f:
    f.write(private_key)

# 保存公钥到文件
public_key = gpg.export_keys(key.fingerprint, False)
with open('public_key.asc', 'w') as f:
    f.write(public_key)


print("RSA 密钥对已生成并保存到 private_key.pem 和 public_key.pem 文件中")
