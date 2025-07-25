# 结构化数据(表格)

行列结构:表格的每一列有明确的字段名和数据类型（如数字、日期、文本），每一行代表一条记录，计算机可以快速解析和操作。

# 什么是数据分析？

数据分析就是将数据转换成“有用”信息的过程。

当一个参数里有多个元素时，用[]括起来，表示这是一个参数。如果不括起来，就成了多个参数了。

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
 


---





# Pandas 示例：销售数据分析全流程

以下是一个综合性的 Pandas 示例，涵盖大纲中的所有核心知识点（从基础操作到高级功能），并通过一个完整的销售数据分析项目串联起来。我们将使用模拟数据演示数据处理全流程。

## 功能需求
1. 创建和操作 DataFrame（基础操作）。
2. 数据清洗（处理缺失值、重复值、异常值）。
3. 数据类型转换与字符串处理。
4. 数据筛选、排序和聚合。
5. 分组统计与透视表。
6. 时间序列处理。
7. 性能优化技巧。
8. 数据导出与可视化（结合 Matplotlib）。

## 完整代码

```python
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

# ====================== 1. 基础操作 ======================
# 创建 DataFrame（模拟销售数据）
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Product': ['A', 'B', 'A', 'C', 'B'],
    'Region': ['East', 'West', 'East', 'North', 'South'],
    'Sales': [100, 200, np.nan, 150, 180],  # 包含缺失值
    'Price': [10.5, 20.3, 15.0, 12.8, 18.2]
}
df = pd.DataFrame(data)

# 查看数据
print("原始数据：")
print(df.head())

# ====================== 2. 数据清洗 ======================
# 处理缺失值：填充销售额的缺失值为该产品的平均值
product_mean_sales = df.groupby('Product')['Sales'].transform('mean')
df['Sales'] = df['Sales'].fillna(product_mean_sales)

# 删除重复值（如果存在）
df = df.drop_duplicates()

# 处理异常值：将销售额大于200的标记为异常（假设200是合理上限）
df['Is_Outlier'] = df['Sales'] > 200

# ====================== 3. 数据类型转换与字符串处理 ======================
# 转换日期格式
df['Date'] = pd.to_datetime(df['Date'])

# 提取月份和季度
df['Month'] = df['Date'].dt.month
df['Quarter'] = df['Date'].dt.quarter

# 字符串操作：将产品名称转为大写
df['Product'] = df['Product'].str.upper()

# ====================== 4. 数据筛选与排序 ======================
# 筛选东部地区的数据
east_data = df[df['Region'] == 'East']

# 筛选销售额大于150的记录
high_sales = df[df['Sales'] > 150]

# 按销售额降序排序
sorted_df = df.sort_values('Sales', ascending=False)

# ====================== 5. 数据聚合与分组 ======================
# 按产品分组计算总销售额和平均价格
product_stats = df.groupby('Product').agg({
    'Sales': ['sum', 'mean'],
    'Price': 'mean'
})
print("\n按产品分组的统计：")
print(product_stats)

# 多列分组：按产品和地区分组计算销售总额
grouped_stats = df.groupby(['Product', 'Region'])['Sales'].sum().reset_index()
print("\n按产品和地区分组的销售总额：")
print(grouped_stats)

# ====================== 6. 透视表 ======================
# 创建透视表：产品 vs 地区，汇总销售额
pivot_table = pd.pivot_table(df, values='Sales', index='Product', columns='Region', aggfunc='sum', fill_value=0)
print("\n透视表：产品 vs 地区的销售总额")
print(pivot_table)

# ====================== 7. 时间序列处理 ======================
# 设置日期为索引
df_time = df.set_index('Date')

# 按月份重采样计算月度销售总额
monthly_sales = df_time['Sales'].resample('M').sum()
print("\n月度销售总额：")
print(monthly_sales)

# 计算7天滑动平均销售额
rolling_avg = df_time['Sales'].rolling(window=2).mean()  # 窗口设为2天（示例数据较少）
print("\n2天滑动平均销售额：")
print(rolling_avg)

# ====================== 8. 性能优化 ======================
# 使用更高效的数据类型（如将字符串转换为分类类型）
df['Product'] = df['Product'].astype('category')
df['Region'] = df['Region'].astype('category')

# 避免链式赋值（推荐使用 .loc）
# 错误示范：df[df['Sales'] > 150]['Price'] = 0  # 可能无法生效
# 正确做法：
df.loc[df['Sales'] > 150, 'Price'] = 0  # 将高销售额产品的价格设为0（模拟促销）

# ====================== 9. 数据导出 ======================
# 导出为CSV
df.to_csv('sales_data_cleaned.csv', index=False)

# 导出为Excel（带多个Sheet）
with pd.ExcelWriter('sales_report.xlsx') as writer:
    df.to_excel(writer, sheet_name='Raw Data', index=False)
    product_stats.to_excel(writer, sheet_name='Product Stats')
    pivot_table.to_excel(writer, sheet_name='Pivot Table')

# ====================== 10. 数据可视化 ======================
# 绘制产品销售额柱状图
plt.figure(figsize=(10, 5))
product_sales = df.groupby('Product')['Sales'].sum()
product_sales.plot(kind='bar', color=['blue', 'green', 'red'])
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales (万元)')
plt.grid(axis='y')
plt.savefig('sales_by_product.png')  # 保存图片
plt.show()

# 绘制时间序列折线图
plt.figure(figsize=(10, 5))
df_time['Sales'].plot(marker='o')
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Sales (万元)')
plt.grid(True)
plt.savefig('sales_trend.png')
plt.show()
```

## 代码解析（对应大纲知识点）

| **知识点**         | **代码实现**                                                                 |
|--------------------|------------------------------------------------------------------------------|
| 基础操作           | DataFrame 创建、head() 查看数据。                                             |
| 数据清洗           | 缺失值填充 (fillna)、去重 (drop_duplicates)、异常值标记。                     |
| 数据类型转换       | to_datetime 转换日期、astype('category') 优化分类数据。                        |
| 字符串处理         | str.upper() 转换产品名称为大写。                                              |
| 数据筛选与排序     | 布尔索引 (df[df['Region'] == 'East'])、sort_values() 排序。                    |
| 数据聚合           | groupby() + agg() 分组统计。                                                  |
| 透视表             | pd.pivot_table() 多维汇总。                                                   |
| 时间序列           | resample() 重采样、rolling() 滑动窗口计算。                                   |
| 性能优化           | 分类数据类型 (astype('category'))、避免链式赋值。                              |
| 数据导出           | to_csv() 和 ExcelWriter 导出多 Sheet。                                         |
| 可视化             | matplotlib 绘制柱状图和折线图。                                               |

## 生成的文件
- **CSV 文件**：`sales_data_cleaned.csv`（清洗后的数据）。
- **Excel 报表**：`sales_report.xlsx`（包含原始数据、统计表和透视表）。
- **图片**：`sales_by_product.png` 和 `sales_trend.png`（可视化结果）。

## 如何扩展？
1. **大数据处理**：结合 Dask 或分块读取 (chunksize) 处理超大数据集。
2. **自动化报告**：用 Jupyter Notebook + Markdown 生成交互式报告。
3. **数据库集成**：从 SQL 数据库直接读取数据（pd.read_sql()）。

这个示例覆盖了 Pandas 的全流程操作，适合直接运行学习！如果有任何问题，欢迎提问。 🐼📊
