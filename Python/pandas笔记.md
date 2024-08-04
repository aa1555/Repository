# 单词：

▲row：行 ▲column：列▲separate：分开，分离▲skip：跳过▲Frame：框架

# 数据类型与新建文件
|数据类型|说明|新建方法|
|  ----  | ----   | ----  |  
csv、tsv、txt|用逗号分隔、tab分割的纯文本文件|pd.to_csv|
excel|xls或xlsx|pd.to_excel|
mysql|关系数据库表|pd.to_sql|

DataFrame：二维数组

array：一维数据（一列或一行）

注意，一维数据是指一列或一行，一维数组是只有一行。

## 创建Excel/csv
```python
import pandas as pd                                 
path = '新建空白文件.xlsx'                    
data=pd.DataFrame({'序号':[1,2,3],'姓名':['叶问','李小龙','孙兴华']})         
data=data.set_index('序号')  # 将id设置为索引,如果不设置，左边会多出一个索引列。
data.to_excel(path)            
print('新建空白文件.xlsx成功')     
```
只有实现了to_excel方法的对象才能使用这个方法，显然data对象实现了这个方法 。

这段代码的关键步骤是`data.to_excel(path)` ，有了这个步骤，缺data就去创建data，缺path就去创建path。也就是说，前面的导入库，创建data，创建path，这些步骤都是为`data.to_excel(path)`做准备，没有它，前面的准备白费。这就是根据目的倒推程序的思维方式。

创建csv也是一样，把Excel改成csv就行了。

# 读取数据（用.read_csv方法）

| 数据类型| 	说明| 	读取方法| 
|  ----  | ----   | ----  |  
| csv、tsv、txt	| 默认逗号分隔| 	pd.read_csv
| csv、tsv、txt| 	默认\t分隔| 	pd.read_table
| excel	| xls或xlsx| 	pd.read_excel
| mysql	| 关系数据库表| 	pd.read_sql

例：
```python
import pandas as pd
path = '读取文件.csv'
read_data = pd.read_csv(path,sep=',',header=None,names=['姓名','年龄','地址','电话','入职日期'],encoding='utf-8',index_col='入职日期',nrows=3)
print(read_data)        
```
## read_csv的参数

|参数	|描述|
|  ----  | ----   | 
|sep	|分隔符或正则表达式 sep='\s+'。即设置以什么符号分隔。|
|header	|列名(表头)的行号，默认0（第一行），如果没有列名应该为None。即设置以第几行为表头，默认第一行。|
|names	|列名（表头），与header=None一起使用。如果没有表头，可以将表头传入本参数，自定义表头。|
|index_col	|索引的列号或列名，可以是一个单一的名称或数字，也可以是一个分层索引。即设置第几列为索引。将参数设置为False，可以在文本输出中不显示索引。ps：行的索引是列，列的索引是行。|
|skiprows	|从文件开始处，需要跳过的行数或行号列表。即设置哪些行不需要读取。|
|encoding	|文本编码，例如utf-8|
|nrows	|从文件开头处读入的行数。即需要读取前几行。|

这些参数根据需要传入，除了第一个参数要指定被读取文件的路径，不能省略，剩下的都可以省略。省略即使用默认参数。

# 写入数据（用.to_excel方法）

自己设置并写入表头【第一种方法】
```python
import pandas as pd
path = 'c:/pandas/读取文件.xlsx'
read_date = pd.read_excel(path,header=None)
read_date.columns=['序号','姓名','年龄','地址','电话','入职日期']  # 给每个列重复设置表头
read_date=read_date.set_index('序号')          # 重新指定索引列
print(read_date.columns)          # 查看列名列表
read_date.to_excel('path')          # 写入到Excel文件
```
自己设置并写入表头【第二种方法】
```python
import pandas as pd
path = 'c:/pandas/读取文件.xlsx'
read_date = pd.read_excel(path,header=None,index_col='序号')
read_date.columns=['序号','姓名','年龄','地址','电话','入职日期']  # 给每个列重复设置表头
read_date=read_date.set_index('序号',inplace=True)          # 只在index上面改,不要生成新的
print(read_date.columns)          # 查看列名列表，index和columns是分开的
read_date.to_excel('path')          # 写入到Excel文件
```

# pandas数据结构

## Series

常用方法

```python
date.index #查看索引
date.values #查看数值
date.isnull() #查看为空的，返回布尔型，为空返回Ture，反之返回False
date.notnull() # 查看不为空,不为空返回Ture
date.sort_index() #按索引排序
date.sort_values() #按数值排序
```

## DataFrame

```python
import pandas as pd
date=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['a','b','c'])  #columns列索引
print(date)  
print(date['a'][0] )   # 取a列0行
print(date.loc[0]['a'] )  # 取0行，a列
print(date.iloc[0][0] )   # 取0行，0列，根据号取值，不根据列名
print(date[['a','b']])  # 取a列和b列，这个索引就是以一个索引的列表作为一个元素，代替一个索引值元素。
```
`date['a'][0]`:取a列0行

`date.loc[0]['a']`:取0行，a列

`date.iloc[0][0]`:取0行，0列，根据号取值，不根据名

`date[['a','b']]`:取a列和b列

### 多个字典序列创建DataFrame
```python

import pandas as pd
dict = {
        '姓名':['孙兴华','李小龙','叶问'],
        '年龄':[20,80,127],
        '功夫':['撸铁','截拳道','咏春']
        }
date = pd.DataFrame(dict)
print(date)
print(date.dtypes)    # 返回每一列的类型
print(date.columns) # 返回列索引，以列表形式返回：[列名1，列名2，…]
print(date.index)      # 返回行索引，（起始，结束，步长）
```

`date.columns`：返回列索引

`date.index`：返回行索引

`date.loc[2]['b']`:查询第2行第b列

## DataFrame常用方法
```python
date.head( 5 ) #查看前5行
date.tail( 3 ) #查看后3行
date.values #查看数值
date.shape #查看行数、列数
date.fillna(0) #将空值填充0
date.replace( 1, -1) #将1替换成-1
date.isnull() #查找数据中出现的空值
date.notnull() #非空值
date.dropna() #删除空值
date.unique() #查看唯一值
date.reset_index() #修改、删除，原有索引，详见例1
date.columns #查看数据的列名
date.index #查看索引
date.sort_index() #索引排序 
date.sort_values() #值排序
pd.merge(数据1,数据1) #合并
pd.concat([数据1,数据2]) #合并，与merge的区别，自查
pd.pivot_table( date ) #用df做数据透视表（类似于Excel的数透）
```
例1：
```python
import pandas as pd
path = 'c:/pandas/读取文件.xlsx'
read_date = pd.read_excel(path,header=None,names=['序号','姓名','年龄','手机','地址','入职日期'],index_col='序号')
print(read_date.reset_index(drop=True)) # 索引被直接删除
print(read_date.reset_index(drop=False)) # 索引列会被还原为普通列
```
 
