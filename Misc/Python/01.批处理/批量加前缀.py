import os

directory = r"C:\Users\aa155\Desktop\A春 - 副本 - 副本"                #设置文件夹路径
# 设置要添加的前缀
prefix = '徐建军_'                                                     #设置需要添加的前缀

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
