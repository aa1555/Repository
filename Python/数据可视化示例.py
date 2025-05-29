import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 生成模拟数据
categories = ['电子产品', '服装', '食品', '家居用品', '图书', '美妆护肤', '母婴用品', '运动户外']
months = ['1月', '2月', '3月', '4月', '5月', '6月']

# 创建DataFrame
data = {
    '月份': [],
    '商品类别': [],
    '销售额(万元)': [],
    '销售量(件)': []
}

np.random.seed(42)  # 设置随机种子保证可重复性

for month in months:
    for category in categories:
        sales = round(np.random.uniform(5, 200), 2)  # 销售额在5-200万元之间
        quantity = round(np.random.uniform(50, 800), 0)  # 销售量在50-800件之间
        data['月份'].append(month)
        data['商品类别'].append(category)
        data['销售额(万元)'].append(sales)
        data['销售量(件)'].append(quantity)

df = pd.DataFrame(data)

# 1. 不同商品类别的月度销售额对比
monthly_sales = df.groupby(['月份', '商品类别'])['销售额(万元)'].sum().unstack()

plt.figure(figsize=(12, 6))
monthly_sales.plot(kind='bar', stacked=False)
plt.title('不同商品类别的月度销售额对比')
plt.xlabel('月份')
plt.ylabel('销售额(万元)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. 各商品类别销售占比
category_sales = df.groupby('商品类别')['销售额(万元)'].sum()

plt.figure(figsize=(8, 8))
plt.pie(category_sales, labels=category_sales.index, autopct='%1.1f%%', startangle=140)
plt.title('各商品类别销售占比')
plt.axis('equal')  # 保证饼图为圆形
plt.show()

# 3. 销售额与销售量的关系
sample_categories = np.random.choice(categories, 3, replace=False)

plt.figure(figsize=(10, 6))
for category in sample_categories:
    subset = df[df['商品类别'] == category]
    plt.scatter(subset['销售量(件)'], subset['销售额(万元)'], label=category)

plt.title('销售额与销售量的关系')
plt.xlabel('销售量(件)')
plt.ylabel('销售额(万元)')
plt.legend()
plt.grid(True)
plt.show()

# 4. 每月销售额趋势
monthly_total = df.groupby('月份')['销售额(万元)'].sum()

plt.figure(figsize=(10, 6))
monthly_total.plot(kind='line', marker='o')
plt.title('每月销售额趋势')
plt.xlabel('月份')
plt.ylabel('销售额(万元)')
plt.grid(True)
plt.show()