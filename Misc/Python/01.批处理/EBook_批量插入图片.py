f = ""   # 为后面使用f += d + "\n\n"做准备

for i in range(1,80):                                                           #设置要插入的图片数量
    a = '''  <div class="duokan-image-single">

    <img class="duokan-image" src="../Images/'''

    b = f'B ({i}).png'                                                          #设置图片文件名

    c = '''"/> 

  </div>'''
    
    d = a+b+c #拼接数据

    f += d + "\n\n"    # 把每组数据都添加到f变量中，且每组数据之间都有一个空格。

# 写入txt文件
with open(r"C:\Users\aa155\Desktop\新建文件夹\在epub中插入图片.txt", 'w', encoding='utf-8') as file:    #设置txt路径和文件名
    file.write(f)