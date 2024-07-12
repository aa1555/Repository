import os

directory = r"C:\Users\aa155\Desktop\新建文件夹"                                 # 设置目录路径

name_suffix = '_delete_me'                                                      # 设置要删除的文件名后缀

# 遍历目录中的所有文件
for filename in os.listdir(directory):
    # 获取文件的完整路径
    filepath = os.path.join(directory, filename)
    # 如果是文件，则进行操作
    if os.path.isfile(filepath):
        # 分离文件名和扩展名
        name, extension = os.path.splitext(filename)
        # 检查文件名是否包含要删除的后缀
        if name.endswith(name_suffix):
            # 删除文件名中的后缀
            new_name = name[:-len(name_suffix)] + extension
            # 新的文件完整路径
            new_filepath = os.path.join(directory, new_name)
            # 重命名文件
            os.rename(filepath, new_filepath)
            print(f"Renamed '{filename}' to '{new_name}'")
