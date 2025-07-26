
# 示例：销售数据分析报表（使用 openpyxl）

> 本示例综合演示 `openpyxl` 大纲中的所有核心知识点：  
> 基础操作、样式、公式、图表、合并单元格、大数据处理等。

## 功能需求

- 创建一个新的 Excel 文件。
- 写入销售数据（模拟数据）。
- 设置单元格样式（字体、颜色、边框等）。
- 使用公式计算总销售额和平均值。
- 插入柱状图可视化销售数据。
- 合并单元格作为标题。
- 调整列宽和行高。
- 保存文件。

---

## 完整代码

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
    cell.border = Border(
        left=Side(style='thin'), right=Side(style='thin'),
        top=Side(style='thin'), bottom=Side(style='thin')
    )

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
        cell.border = Border(
            left=Side(style='thin'), right=Side(style='thin'),
            top=Side(style='thin'), bottom=Side(style='thin')
        )

# 5. 使用公式计算总销售额和平均值
total_row = ws.max_row + 2
ws.cell(row=total_row, column=1).value = "总计"
ws.cell(row=total_row, column=3).value = f"=SUM(C3:C{ws.max_row})"

ws.cell(row=total_row + 1, column=1).value = "平均值"
ws.cell(row=total_row + 1, column=3).value = f"=AVERAGE(C3:C{ws.max_row})"

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

data = Reference(ws, min_col=3, min_row=2, max_row=ws.max_row)
categories = Reference(ws, min_col=1, min_row=2, max_row=ws.max_row)

chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

ws.add_chart(chart, "F2")

# 7. 调整列宽和行高
ws.column_dimensions['A'].width = 15
ws.column_dimensions['B'].width = 10
ws.column_dimensions['C'].width = 15
ws.column_dimensions['D'].width = 15

for row in ws.iter_rows(min_row=1, max_row=ws.max_row):
    row[0].alignment = Alignment(horizontal="center")

# 8. 保存文件
wb.save("res/sales_report.xlsx")
print("Excel 文件已生成：sales_report.xlsx")
```

---

## 知识点对应说明

| 知识点       | 代码实现示例                                |
|--------------|---------------------------------------------|
| 基础操作     | `Workbook()`、`ws.append()`、`wb.save()`    |
| 样式设置     | `Font`、`PatternFill`、`Border`、`Alignment` |
| 公式计算     | `SUM()`、`AVERAGE()`                         |
| 图表生成     | `BarChart`、`Reference`、`add_chart()`       |
| 合并单元格   | `ws.merge_cells()`                           |
| 大数据处理   | `iter_rows()` 高效遍历                      |
| 文件操作     | `wb.save()` 保存 Excel 文件                 |

---

## Excel 文件预期效果

- **标题：** 合并单元格 + 居中 + 蓝底白字  
- **表头：** 加粗字体 + 浅蓝背景 + 边框  
- **数据区域：** 统一边框 + 居中对齐  
- **公式行：** 总销售额和平均值自动计算  
- **图表：** 柱状图展示各产品季度销售额

---

## 如何扩展？

- 使用 `pandas` 读取数据库或 CSV 动态生成数据。
- 添加其他图表类型如：折线图、饼图等。
- 使用模板文件并动态填充数据，保留 Excel 格式与样式。
