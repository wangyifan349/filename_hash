import os
import sqlite3

# 连接到 SQLite3 数据库,确保数据库存在，并且表结构正确。
conn = sqlite3.connect('file_names.db')
cursor = conn.cursor()

# 输入你要恢复的文件路径和目录
recovery_folder_path = './1'  # 这是你想要恢复文件的目录
#os.makedirs(recovery_folder_path, exist_ok=True)

# 遍历要恢复的文件夹
for root,dir, files in os.walk(recovery_folder_path):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        # 获取文件名和扩展名
        name, ext = os.path.splitext(file_name)
        # 查询数据库以获取原始文件名
        cursor.execute('SELECT original_name FROM file_names WHERE hash_value = ?', (name,))
        result = cursor.fetchone()
        if result:
            original_name = result[0]
            new_file_path = os.path.join(root, original_name)
            # 重命名文件
            os.rename(file_path, new_file_path)
        else:
            print(f"数据库中未找到哈希值: {name}")

# 关闭数据库连接
conn.close()
