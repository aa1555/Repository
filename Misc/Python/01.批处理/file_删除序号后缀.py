import os
import re

def rename_file(path):
    # 遍历指定路径下的所有文件
    for filename in os.listdir(path):
        # 分离文件名和扩展名
        base_name, ext = os.path.splitext(filename)
        
        # 使用正则表达式删除序号后缀
        new_base_name = re.sub(r'\d+$', '', base_name)
        
        # 重新组合文件名和扩展名
        new_filename = new_base_name + ext
        
        # 获取文件的原始路径和新路径
        old_file_path = os.path.join(path, filename)
        new_file_path = os.path.join(path, new_filename)
        
        # 检查新的文件名是否已经存在
        if not os.path.exists(new_file_path):         # 如果重命名后的文件名已存在，则跳过，不存在，则重命名。
            # 如果新的文件名不存在，重命名文件
            os.rename(old_file_path, new_file_path)

# 调用函数，传入你想要修改文件名的目录
rename_file(r"C:\Users\aa155\Desktop\新建文件夹")
