a=range





c=a

print("\n一、打印该对象:\n",c,"\n\n")

print("二、该对象的类型:\n",type(c),"\n\n")

print("三、该对象的方法：")
for i in dir(c):
    print(i,"    ",end="")
