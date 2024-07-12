import os

directory = r"C:\Users\aa155\Desktop\新建文件夹"                                 # 设置目录路径

old_extension = '.txt'                                                          # 设置要替换的旧扩展名

new_extension = '.jpg'                                                          # 设置新的扩展名

# 遍历目录中的所有文件
for filename in os.listdir(directory):
    # 获取文件的完整路径
    filepath = os.path.join(directory, filename)
    # 如果是文件，则进行操作
    if os.path.isfile(filepath):
        # 检查文件扩展名是否为要替换的旧扩展名
        if filename.endswith(old_extension):
            # 生成新的文件名
            new_filename = filename[:-len(old_extension)] + new_extension
            # 新的文件完整路径
            new_filepath = os.path.join(directory, new_filename)
            # 重命名文件
            os.rename(filepath, new_filepath)
            print(f"Renamed '{filename}' to '{new_filename}'")
