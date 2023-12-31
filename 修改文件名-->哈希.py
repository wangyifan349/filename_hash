import os
import hashlib
import sqlite3
import secrets  # 导入secrets模块生成生成随机盐用

# 连接到 SQLite3 数据库
conn = sqlite3.connect('file_names.db')
cursor = conn.cursor()
# 创建文件名存储表（包括 original_name、hash_value 和 salt 列）
cursor.execute('''CREATE TABLE IF NOT EXISTS file_names
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   original_name TEXT,
                   hash_value TEXT,
                   salt TEXT)''')
conn.commit()

folder_path = './1'  # 填写你的文件路径

#由于我是在Linux下开发的，windows的路径问题我没有考虑，windows可能修改正确的路径，Linux直接用就可以了。
#linux_path = windows_path.replace('\\', '/')
#windows_path = linux_path.replace('/', '\\')


for root,dir, files in os.walk(folder_path):# 遍历文件夹及其子文件夹
    for file_name in files:
        file_path = os.path.join(root, file_name)
        # 获取文件名和扩展名
        name, ext = os.path.splitext(file_name)
        # 生成随机盐
        salt = secrets.token_hex(16)  # 生成一个16字节的随机十六进制值作为盐
        name_with_salt = name + salt
        # 计算文件名的哈希值
        hash_value = hashlib.blake2b(name_with_salt.encode(), digest_size=16).hexdigest()  # 32 字节作为摘要大小
        # 构建新文件名
        new_file_name = f"{hash_value}{ext}"
        # 处理重名文件
        index = 1
        while os.path.exists(os.path.join(root, new_file_name)):
            new_file_name = f"{hash_value}_{index}{ext}"
            index += 1
        os.rename(file_path, os.path.join(root, new_file_name))# 重命名文件
        #print(f"重命名: {file_name} -> {new_file_name}")
        # 将原始文件名、哈希值和随机盐存储到数据库
        cursor.execute('INSERT INTO file_names (original_name, hash_value, salt) VALUES (?, ?, ?)', (file_name, hash_value, salt))
        
conn.commit()
# 关闭数据库连接
conn.close()
