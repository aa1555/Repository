
# 使用 matplotlib 进行可视化示例

matplotlib 是 Python 中最基础、强大的绘图库之一，支持绘制折线图、柱状图、饼图、散点图等。以下是一个覆盖常用图形类型的完整示例：

## ✅ 示例文件名：`matplotlib_demo.py`

```python
import matplotlib.pyplot as plt
import numpy as np

# 设置中文和负号正常显示（可选）
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# -----------------------------
# 1. 折线图 Line Chart
# -----------------------------
x = np.arange(1, 6)
y = np.array([10, 20, 15, 25, 30])

plt.figure(figsize=(6, 4))
plt.plot(x, y, marker='o', linestyle='-', color='b', label='销售额')
plt.title("销售趋势折线图")
plt.xlabel("月份")
plt.ylabel("金额")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("line_chart.png")
plt.close()

# -----------------------------
# 2. 柱状图 Bar Chart
# -----------------------------
departments = ['HR', 'IT', 'Finance', 'Sales']
salaries = [50000, 70000, 65000, 60000]

plt.figure(figsize=(6, 4))
plt.bar(departments, salaries, color='skyblue')
plt.title("各部门平均薪资")
plt.ylabel("薪资")
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.close()

# -----------------------------
# 3. 饼图 Pie Chart
# -----------------------------
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [40, 25, 20, 15]

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("编程语言占比")
plt.tight_layout()
plt.savefig("pie_chart.png")
plt.close()

# -----------------------------
# 4. 散点图 Scatter Plot
# -----------------------------
np.random.seed(42)
x = np.random.rand(50)
y = np.random.rand(50)

plt.figure(figsize=(6, 4))
plt.scatter(x, y, color='purple', alpha=0.7)
plt.title("散点图示例")
plt.xlabel("X 值")
plt.ylabel("Y 值")
plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.close()

print("图表已保存：line_chart.png, bar_chart.png, pie_chart.png, scatter_plot.png")
```

---

## ✅ 安装依赖

```bash
pip install matplotlib
```

---

## ✅ 常见图类型总结

| 图形 | 说明 |
|------|------|
| 折线图（plot） | 展示趋势变化 |
| 柱状图（bar） | 类别对比 |
| 饼图（pie） | 比例分布 |
| 散点图（scatter） | 分布、相关性 |
| 直方图（hist） | 分布密度 |
| 箱线图（boxplot） | 数据分布与离群值 |

---

matplotlib 是可视化的基石，建议搭配 seaborn、pandas.plot 进一步提升美观度和效率！
