import os

directory = r"C:\Users\aa155\Desktop\新建文件夹"                                       #设置文件夹路径
# 设置新文件名的前缀
new_filename_prefix = ''                                                              #修改前缀
# 获取当前目录下所有文件列表
files = os.listdir(directory)

# 遍历文件列表
for index, file in enumerate(files,start=1):     # start=1 从1开始计数
    # 分离文件名和扩展名
    filename, file_extension = os.path.splitext(file)
    # 忽略目录
    if os.path.isdir(file):
        continue  # 
    # 构造新的文件名
    new_filename = new_filename_prefix + str(index).zfill(3) + file_extension

    print(new_filename)
    # 重命名文件
    os.rename(os.path.join(directory, file), os.path.join(directory, new_filename))
    print(f'文件"{file}"已重命名为"{new_filename}"')

'''
使用这个脚本前，请确保以下几点：

脚本位于要修改文件名的目录中，或者修改directory变量以指向正确的目录。
new_filename_prefix变量设置为你想要的新文件名前缀。
脚本运行前备份重要文件，以防止意外丢失。
请谨慎使用此脚本，因为文件重命名是不可逆的，一旦执行，原始文件名将无法恢复（除非有备份）。
在运行脚本之前，请确保您已经测试过脚本并且理解其功能。

str(index).zfill(3)确保序号部分是三位数字，不足部分用0填充。
例如，1会被格式化为001，10会被格式化为010，以此类推。
若要从1而不是001开始，就把.zfill(3)删掉即可。

在enumerate函数中，start参数用于指定计数开始的值。
默认情况下，enumerate函数的计数是从0开始的，但通过设置start参数，你可以改变计数的起始值。

os.path.isdir(file)检查file是否是一个存在的目录。如果file是目录，它将返回True；如果不是，它将返回False。
continue：这是一个控制流语句，用于跳过当前循环的剩余部分，并立即开始下一次循环迭代。
在这里当files目录，返回true，执行continue，表示跳过它。
'''