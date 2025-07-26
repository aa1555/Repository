以下是一个综合示例，涵盖 `openpyxl` 大纲中的所有核心知识点（基础操作、样式、公式、图表、合并单元格、大数据处理等）。我们将创建一个**销售数据分析报表**，包含动态数据填充、样式美化、公式计算、图表生成和合并单元格等功能。

---

### **示例：销售数据分析报表**
#### **功能需求**
1. 创建一个新的 Excel 文件。
2. 写入销售数据（模拟数据）。
3. 设置单元格样式（字体、颜色、边框等）。
4. 使用公式计算总销售额和平均值。
5. 插入柱状图可视化销售数据。
6. 合并单元格作为标题。
7. 调整列宽和行高。
8. 保存文件。

---

### **完整代码**
```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
from openpyxl.chart import BarChart, Reference
from openpyxl.utils import get_column_letter

# 1. 创建工作簿和工作表
wb = Workbook()
ws = wb.active
ws.title = "Sales Report"

# 2. 写入标题（合并单元格）
ws.merge_cells('A1:D1')
title_cell = ws['A1']
title_cell.value = "2023年销售数据分析报表"
title_cell.font = Font(size=16, bold=True, color="FFFFFF")
title_cell.fill = PatternFill(start_color="4F81BD", end_color="4F81BD", fill_type="solid")
title_cell.alignment = Alignment(horizontal="center")

# 3. 写入表头
headers = ["产品", "季度", "销售额（万元）", "同比增长"]
ws.append(headers)

# 设置表头样式
for col in range(1, len(headers) + 1):
    cell = ws.cell(row=2, column=col)
    cell.font = Font(bold=True)
    cell.fill = PatternFill(start_color="DCE6F1", end_color="DCE6F1", fill_type="solid")
    cell.border = Border(left=Side(style='thin'), right=Side(style='thin'), 
                         top=Side(style='thin'), bottom=Side(style='thin'))

# 4. 写入模拟数据
sales_data = [
    ["产品A", "Q1", 120, 0.15],
    ["产品A", "Q2", 150, 0.20],
    ["产品A", "Q3", 180, 0.25],
    ["产品A", "Q4", 200, 0.30],
    ["产品B", "Q1", 80, 0.10],
    ["产品B", "Q2", 90, 0.12],
    ["产品B", "Q3", 110, 0.18],
    ["产品B", "Q4", 130, 0.22],
]

for row in sales_data:
    ws.append(row)

# 设置数据区域样式
for row in ws.iter_rows(min_row=3, max_row=ws.max_row, min_col=1, max_col=4):
    for cell in row:
        cell.border = Border(left=Side(style='thin'), right=Side(style='thin'), 
                             top=Side(style='thin'), bottom=Side(style='thin'))

# 5. 使用公式计算总销售额和平均值
total_row = ws.max_row + 2
ws.cell(row=total_row, column=1).value = "总计"
ws.cell(row=total_row, column=3).value = f"=SUM(C3:C{ws.max_row})"  # 总销售额
ws.cell(row=total_row + 1, column=1).value = "平均值"
ws.cell(row=total_row + 1, column=3).value = f"=AVERAGE(C3:C{ws.max_row})"  # 平均销售额

# 设置公式单元格样式
for row in [total_row, total_row + 1]:
    for col in [1, 3]:
        cell = ws.cell(row=row, column=col)
        cell.font = Font(bold=True)

# 6. 插入柱状图
chart = BarChart()
chart.title = "各产品季度销售额"
chart.x_axis.title = "产品 & 季度"
chart.y_axis.title = "销售额（万元）"

# 定义数据范围（产品+季度作为分类，销售额作为值）
data = Reference(ws, min_col=3, min_row=2, max_row=ws.max_row)
categories = Reference(ws, min_col=1, min_row=3, max_row=ws.max_row)

chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

# 将图表插入到工作表中
ws.add_chart(chart, "F2")

# 7. 调整列宽和行高
ws.column_dimensions['A'].width = 15  # 产品列宽
ws.column_dimensions['B'].width = 10  # 季度列宽
ws.column_dimensions['C'].width = 15  # 销售额列宽
ws.column_dimensions['D'].width = 15  # 同比增长列宽

for row in ws.iter_rows(min_row=1, max_row=ws.max_row):
    row[0].alignment = Alignment(horizontal="center")  # 第一列居中

# 8. 保存文件
wb.save("res/sales_report.xlsx")
print("Excel 文件已生成：sales_report.xlsx")
```

---

### **代码解析（对应大纲知识点）**
| **知识点**               | **代码实现**                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| **基础操作**             | 创建工作簿 (`Workbook()`)、写入数据 (`ws.append()`)、保存文件 (`wb.save()`)。 |
| **样式设置**             | 字体 (`Font`)、填充 (`PatternFill`)、边框 (`Border`)、对齐 (`Alignment`)。    |
| **公式计算**             | `f"=SUM(C3:C{ws.max_row})"` 和 `f"=AVERAGE(C3:C{ws.max_row})"`。              |
| **图表生成**             | `BarChart`、`Reference` 定义数据范围、`ws.add_chart()` 插入图表。             |
| **合并单元格**           | `ws.merge_cells('A1:D1')`。                                                 |
| **大数据处理**           | 本例数据量较小，但演示了 `ws.iter_rows()` 高效遍历方法。                      |
| **文件操作**             | `wb.save()` 保存为 `.xlsx` 文件。                                           |

---

### **生成的 Excel 文件效果**
1. **标题**：合并单元格 + 居中 + 蓝色背景 + 白色字体。  
2. **表头**：加粗 + 浅蓝色背景 + 边框。  
3. **数据区域**：统一边框 + 居中对齐。  
4. **公式**：自动计算总销售额和平均值。  
5. **图表**：柱状图展示各产品季度销售额。  

---

### **如何扩展？**
1. **动态数据**：替换 `sales_data` 为从数据库或 CSV 读取的真实数据（结合 `pandas`）。  
2. **更多图表**：添加折线图、饼图等（参考 `openpyxl.chart` 文档）。  
3. **模板填充**：预先设计 Excel 模板，在 Python 中填充数据（保留格式）。  

这个示例覆盖了 `openpyxl` 的核心功能，适合直接运行学习！如果有任何问题，欢迎提问。 🚀