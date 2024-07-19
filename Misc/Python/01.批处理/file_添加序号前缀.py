import os

# 设置目标文件夹路径
folder_path = r"C:\Users\aa155\Desktop\新建文件夹"

# 获取文件夹内的所有文件列表
files = os.listdir(folder_path)

# 对文件列表进行排序，确保按照特定顺序添加序号
files.sort()

# 遍历文件列表，为每个文件添加序号
for index, file in enumerate(files, start=1):                  # 从1开始计数
    # 构建新的文件名
    new_file_name = f"{str(index).zfill(3)}.{file}"           # 如果序号前面不需要加.,就把{file}前面的.删掉  .zfill(3)表示至少三位字符，不足时用0补充，如果序号大于或等于100，zfill(3)不会对字符串进行任何修改。
    
    # 构建原文件和新生成的文件的完整路径
    old_file_path = os.path.join(folder_path, file)
    new_file_path = os.path.join(folder_path, new_file_name)
    
    # 重命名文件
    os.rename(old_file_path, new_file_path)
    print(f"Renamed: {file} -> {new_file_name}")
