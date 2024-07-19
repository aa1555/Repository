import os
import re

# 设置目标文件夹路径
folder_path = r"C:\Users\aa155\Desktop\新建文件夹"

# 获取文件夹内的所有文件列表
files = os.listdir(folder_path)

# 定义一个正则表达式来匹配文件名中的序号部分
pattern = re.compile(r'^\d{3}')            # 用正则表达式选中前三位数字

# 遍历文件列表，删除文件名中的序号
for file in files:
    # 使用正则表达式匹配序号
    match = pattern.match(file)
    
    # 如果匹配到序号，则删除序号部分
    if match:
        # 构建新的文件名
        new_file_name = file[match.end():]
        
        # 构建原文件和新生成的文件的完整路径
        old_file_path = os.path.join(folder_path, file)
        new_file_path = os.path.join(folder_path, new_file_name)
        
        # 重命名文件
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {file} -> {new_file_name}")
