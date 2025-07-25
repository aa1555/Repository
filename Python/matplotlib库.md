#### 常用的图表类型及其应用场景:

简单的说，看趋势折线图，比数据柱状图，定关系散点图，查占比饼状图，看分布直方图，找离群箱线图。

<p align="center">
<img src="../Misc/img/choose_your_chart.png" alt="图片加载失败" width="400">
</p>





---




以下是一个综合的 Python 示例，涵盖了 **Matplotlib 学习大纲** 中的主要知识点。这个示例通过一个完整的脚本，展示如何使用 Matplotlib 绘制多种类型的图表（折线图、散点图、柱状图、直方图、饼图、箱线图、3D 图表、动态图表等），并结合 NumPy 和 Pandas 进行数据处理，展示子图、自定义样式、注释、双轴图表等功能。代码中包含详细注释，便于理解每个部分的用途。

为了保持清晰，示例将数据可视化任务集中在分析一个模拟的“销售数据集”上，涵盖大纲中的核心内容。代码使用 Python 和 Matplotlib，适合在 Jupyter Notebook 或标准 Python 环境中运行。

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import seaborn as sns

# 设置 Matplotlib 主题
plt.style.use('seaborn')

# 生成模拟销售数据
np.random.seed(42)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = np.random.normal(1000, 200, 12)  # 模拟月度销售额
profit = sales * np.random.uniform(0.1, 0.3, 12)  # 模拟利润
categories = ['Electronics', 'Clothing', 'Books', 'Food']
category_sales = np.random.randint(200, 800, size=(12, len(categories)))
df = pd.DataFrame(category_sales, index=months, columns=categories)

# 创建 Figure 和子图布局（2x3 网格）
fig, axes = plt.subplots(2, 3, figsize=(18, 10), tight_layout=True)

# 1. 折线图：月度销售额和利润
ax1 = axes[0, 0]
ax1.plot(months, sales, marker='o', linestyle='-', color='b', label='Sales')
ax1_twin = ax1.twinx()  # 双 Y 轴
ax1_twin.plot(months, profit, marker='s', linestyle='--', color='r', label='Profit')
ax1.set_title('Monthly Sales and Profit')
ax1.set_xlabel('Month')
ax1.set_ylabel('Sales ($)', color='b')
ax1_twin.set_ylabel('Profit ($)', color='r')
ax1.grid(True)
ax1.legend(loc='upper left')
ax1_twin.legend(loc='upper right')

# 2. 散点图：销售额与利润的关系
ax2 = axes[0, 1]
scatter = ax2.scatter(sales, profit, s=sales/10, c=profit, cmap='viridis', alpha=0.6)
ax2.set_title('Sales vs Profit')
ax2.set_xlabel('Sales ($)')
ax2.set_ylabel('Profit ($)')
fig.colorbar(scatter, ax=ax2, label='Profit ($)')
ax2.annotate('High Profit', xy=(max(sales), max(profit)), xytext=(max(sales)-200, max(profit)-50),
             arrowprops=dict(facecolor='black', shrink=0.05))

# 3. 柱状图：各品类销售额
ax3 = axes[0, 2]
bottom = np.zeros(len(months))
for category in categories:
    ax3.bar(months, df[category], bottom=bottom, label=category)
    bottom += df[category]
ax3.set_title('Stacked Sales by Category')
ax3.set_xlabel('Month')
ax3.set_ylabel('Sales ($)')
ax3.legend()

# 4. 直方图：销售额分布
ax4 = axes[1, 0]
ax4.hist(sales, bins=5, color='skyblue', edgecolor='black', density=True)
ax4.set_title('Sales Distribution')
ax4.set_xlabel('Sales ($)')
ax4.set_ylabel('Density')

# 5. 饼图：最后一个月的品类销售占比
ax5 = axes[1, 1]
ax5.pie(df.iloc[-1], labels=categories, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
ax5.set_title('Sales Share (Dec)')

# 6. 箱线图：各品类销售分布
ax6 = axes[1, 2]
ax6.boxplot([df[cat] for cat in categories], labels=categories)
ax6.set_title('Sales Distribution by Category')
ax6.set_ylabel('Sales ($)')

# 调整子图间距
plt.tight_layout()

# 保存图表
plt.savefig('sales_analysis.png', dpi=300, bbox_inches='tight')

# 7. 3D 散点图：销售额、利润和月份
fig_3d = plt.figure(figsize=(8, 6))
ax_3d = fig_3d.add_subplot(111, projection='3d')
ax_3d.scatter(range(12), sales, profit, c=profit, cmap='plasma', s=100)
ax_3d.set_xlabel('Month')
ax_3d.set_ylabel('Sales ($)')
ax_3d.set_zlabel('Profit ($)')
ax_3d.set_title('3D Sales and Profit')
plt.savefig('3d_sales.png', dpi=300)

# 8. 动态图表：模拟销售额随时间变化
fig_anim = plt.figure(figsize=(8, 6))
ax_anim = fig_anim.add_subplot(111)
line, = ax_anim.plot([], [], 'b-', marker='o')
ax_anim.set_xlim(0, 11)
ax_anim.set_ylim(0, max(sales) * 1.2)
ax_anim.set_xlabel('Month')
ax_anim.set_ylabel('Sales ($)')
ax_anim.set_title('Dynamic Sales Animation')
ax_anim.grid(True)

def update(frame):
    line.set_data(range(frame + 1), sales[:frame + 1])
    return line,

ani = FuncAnimation(fig_anim, update, frames=len(months), interval=500, blit=True)
ani.save('sales_animation.gif', writer='pillow')

# 显示所有图表
plt.show()
```

---

### **代码说明**
1. **基础功能**（模块 1）：
   - 使用 `plt.style.use('seaborn')` 设置主题。
   - 创建 `Figure` 和 `Axes` 对象，使用 `plt.subplots()` 布局。
   - 保存图表为 PNG 和 GIF 格式。
2. **核心绘图类型**（模块 2）：
   - 折线图：绘制销售额和利润（双 Y 轴）。
   - 散点图：展示销售额与利润的关系，使用颜色映射。
   - 柱状图：堆叠各品类的销售额。
   - 直方图：展示销售额分布。
   - 饼图：显示最后一个月的品类销售占比。
   - 箱线图：比较各品类销售分布。
3. **图表定制**（模块 3）：
   - 设置标题、轴标签、图例和网格。
   - 自定义颜色、透明度和点大小。
   - 使用 Seaborn 调色板美化饼图。
4. **进阶功能**（模块 4）：
   - 双 Y 轴图表：结合折线图显示销售额和利润。
   - 3D 散点图：展示月份、销售额和利润的关系。
   - 动态图表：使用 `FuncAnimation` 创建销售动画。
   - 注释：在散点图中添加箭头和文本。
5. **数据处理**（模块 5）：
   - 使用 NumPy 生成模拟数据。
   - 使用 Pandas DataFrame 组织数据。
   - 结合 Seaborn 的调色板进行美化。
6. **实际应用**（模块 6）：
   - 模拟销售数据分析场景，生成多种图表。
   - 输出专业可视化结果，保存为文件。
7. **Matplotlib 生态**（模块 7）：
   - 结合 Seaborn 进行颜色美化。
   - 使用 `mpl_toolkits.mplot3d` 绘制 3D 图表。
8. **调试与优化**（模块 8）：
   - 使用 `tight_layout()` 避免子图重叠。
   - 优化文件输出（高 DPI 保存）。

### **运行说明**
- **依赖**：确保安装了 `numpy`、`pandas`、`matplotlib` 和 `seaborn`（`pip install numpy pandas matplotlib seaborn`）。
- **环境**：推荐在 Jupyter Notebook 中运行，以便逐块查看图表。
- **输出**：
  - 生成 `sales_analysis.png`（综合图表）。
  - 生成 `3d_sales.png`（3D 图表）。
  - 生成 `sales_animation.gif`（动态图表）。
- **中文支持**：如果遇到中文乱码，请设置 Matplotlib 的字体，例如 `plt.rcParams['font.sans-serif'] = ['SimHei']`（Windows）或 `['Arial Unicode MS']`（macOS）。

如果需要更详细的某个部分的代码、额外的练习，或针对特定知识点的扩展示例，请告诉我！