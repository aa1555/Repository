# directory（目录）

import pandas

# 获取math模块的属性列表
math_attributes = dir(pandas)    # dir()函数用于列出对象的所有属性和方法。

# 使用循环打印每个属性，每个属性占一行
for attribute in math_attributes:
    print(attribute)
