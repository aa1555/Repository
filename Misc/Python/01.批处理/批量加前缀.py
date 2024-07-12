import os

directory = r"C:\Users\aa155\Desktop\新建文件夹"                #设置文件夹路径

prefix = '前缀_'                                               #设置需要添加的前缀

# 获取当前目录下所有文件和目录列表
files_and_dirs = os.listdir(directory)

# 遍历文件和目录列表
for item in files_and_dirs:
    # 检查是否是文件
    if os.path.isfile(os.path.join(directory, item)):
        # 构造新的文件名
        new_name = prefix + item
        # 重命名文件
        os.rename(os.path.join(directory, item), os.path.join(directory, new_name))
        print(f'文件"{item}"已重命名为"{new_name}"')
