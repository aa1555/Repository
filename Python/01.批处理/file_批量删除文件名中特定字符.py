import os

def rename_files(directory):
    for filename in os.listdir(directory):
        # 拼接完整文件路径
        old_path = os.path.join(directory, filename)
        
        # 跳过目录，只处理文件
        if not os.path.isfile(old_path):
            continue
        
        # 删除"拷贝"
        new_name = filename.replace("拷贝", "")
        
        # 仅当新名字不同时才重命名
        if new_name != filename:
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
            print(f"重命名: {filename} -> {new_name}")

# 使用示例
directory = r"C:\Users\aa155\Desktop\新建文件夹"  # 替换为你的文件夹路径
rename_files(directory)