
# Pandas 全能学习示例

这是一个尽可能全面覆盖 Pandas 常用知识点的 `.py` 文件示例，适合学习和参考。

---

## ✅ 示例文件名：`pandas_all_in_one_demo.py`

```python
import pandas as pd
import numpy as np

# ----------------------------
# 1. 创建 DataFrame 和 Series
# ----------------------------
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'age': [25, 30, 35, 40, np.nan],
    'salary': [50000, 60000, 70000, 80000, 90000],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'join_date': pd.to_datetime(['2020-01-01', '2019-05-15', '2021-07-23', '2018-11-01', '2022-03-10'])
}

df = pd.DataFrame(data)
print("初始 DataFrame:\n", df, "\n")

# ----------------------------
# 2. Series 操作
# ----------------------------
age_series = df['age']
print("年龄 Series:\n", age_series)
print("平均年龄:", age_series.mean(), "\n")

# ----------------------------
# 3. 选择与切片（loc / iloc）
# ----------------------------
print("第一行数据（iloc）:\n", df.iloc[0])
print("按标签选取某列（loc）:\n", df.loc[:, 'salary'], "\n")

# ----------------------------
# 4. 处理缺失值
# ----------------------------
print("缺失值统计:\n", df.isnull().sum())
df['age'] = df['age'].fillna(df['age'].mean())  # 填充缺失值
print("填补后:\n", df, "\n")

# ----------------------------
# 5. 数据筛选 & 过滤
# ----------------------------
high_salary = df[df['salary'] > 65000]
print("高薪员工:\n", high_salary, "\n")

# ----------------------------
# 6. 新增列 & apply 函数
# ----------------------------
df['seniority'] = df['age'].apply(lambda x: 'Senior' if x >= 35 else 'Junior')
print("增加 seniority 列:\n", df, "\n")

# ----------------------------
# 7. 分组与聚合
# ----------------------------
grouped = df.groupby('department')['salary'].agg(['mean', 'max'])
print("按部门分组统计:\n", grouped, "\n")

# ----------------------------
# 8. 排序 & 排名
# ----------------------------
df_sorted = df.sort_values(by='salary', ascending=False)
df['rank'] = df['salary'].rank(ascending=False)
print("按工资排序:\n", df_sorted, "\n")
print("工资排名:\n", df[['name', 'salary', 'rank']], "\n")

# ----------------------------
# 9. 合并 / 拼接
# ----------------------------
df2 = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'performance': ['A', 'B', 'A', 'C', 'B']
})
merged_df = pd.merge(df, df2, on='name')
print("合并后的数据:\n", merged_df, "\n")

# ----------------------------
# 10. 读写文件（CSV/Excel）
# ----------------------------
df.to_csv('employees.csv', index=False)
# df.to_excel('employees.xlsx', index=False)

# ----------------------------
# 11. 时间序列处理
# ----------------------------
df['year_joined'] = df['join_date'].dt.year
df['month_joined'] = df['join_date'].dt.month
df['tenure_days'] = (pd.to_datetime('today') - df['join_date']).dt.days
print("加入年份 & 在职天数:\n", df[['name', 'year_joined', 'tenure_days']], "\n")

# ----------------------------
# 12. 可视化（简单演示）
# ----------------------------
import matplotlib.pyplot as plt

df.groupby('department')['salary'].mean().plot(kind='bar', title='平均工资 by 部门')
plt.tight_layout()
plt.show()
```

---

## ✅ 用法建议

1. 将上面内容保存为 `pandas_all_in_one_demo.py`
2. 运行前安装依赖：  
```bash
pip install pandas matplotlib openpyxl
```

---

## ✅ 进阶建议（按阶段）

| 阶段 | 推荐练习 |
|------|--------|
| 初级 | 创建DataFrame、索引操作、导入导出文件 |
| 中级 | 分组聚合、apply、自定义函数 |
| 高级 | 多重索引、多表连接、时间序列建模、性能优化（如 `df.query()`） |

---

如果你愿意，我可以帮你继续将这份代码拆成系列教程，包括每个知识点详细解释与图解。欢迎继续探索 🚀
