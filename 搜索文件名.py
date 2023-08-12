#这个程序的实际意义不大，用来搜索已经存在的文件名，通常找到后，直接进入网盘去搜索加密的文件名。
import sqlite3

# 连接到 SQLite3 数据库
conn = sqlite3.connect('file_names.db')
cursor = conn.cursor()

# 输入要查找的文件名
search_file_name = input("请输入要查找的文件名: ")

# 查询数据库以获取哈希值和盐值
cursor.execute('SELECT hash_value, salt FROM file_names WHERE original_name = ?', (search_file_name,))
results = cursor.fetchall()

if results:
    print(f"文件名: {search_file_name}")
    for hash_value, salt in results:
        print(f"哈希值: {hash_value}")
        print(f"盐值: {salt}")
        print("---")
else:
    print(f"未找到文件名: {search_file_name}")

# 关闭数据库连接
conn.close()
