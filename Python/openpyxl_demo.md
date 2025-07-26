
# 使用 openpyxl 读写 Excel 示例

openpyxl 是处理 `.xlsx` 文件的纯 Python 库，适用于更细粒度的 Excel 操作，例如格式、公式、样式等。下面是一个完整的示例：

## ✅ 示例文件名：`openpyxl_demo.py`

```python
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter

# -----------------------------
# 1. 创建并写入 Excel 文件
# -----------------------------
wb = Workbook()
ws = wb.active
ws.title = "员工信息"

# 写入标题行
headers = ['姓名', '年龄', '薪资', '部门']
ws.append(headers)

# 写入内容
data = [
    ['Alice', 25, 50000, 'HR'],
    ['Bob', 30, 60000, 'IT'],
    ['Charlie', 35, 70000, 'Finance'],
    ['David', 40, 80000, 'IT'],
    ['Eva', 28, 90000, 'HR'],
]

for row in data:
    ws.append(row)

# 设置标题行加粗
for col in range(1, len(headers) + 1):
    cell = ws[f'{get_column_letter(col)}1']
    cell.font = Font(bold=True)

# 保存文件
wb.save("openpyxl_employees.xlsx")
print("Excel 文件已保存为 openpyxl_employees.xlsx")

# -----------------------------
# 2. 读取并打印 Excel 文件
# -----------------------------
wb2 = load_workbook("openpyxl_employees.xlsx")
ws2 = wb2["员工信息"]

print("\n读取 Excel 文件内容:")
for row in ws2.iter_rows(values_only=True):
    print(row)
```

---

## ✅ 安装依赖

```bash
pip install openpyxl
```

---

## ✅ 应用场景

| 场景 | 是否适合 openpyxl |
|------|------------------|
| 数据导出 | ✅ |
| 表格格式控制（颜色、字体） | ✅ |
| 写入公式、合并单元格 | ✅ |
| 快速读写大数据 | ❌（速度慢）|
| 与 Pandas 配合 | ✅（pandas 使用 `engine="openpyxl"`）|

---

openpyxl 更适合当你对 **Excel 的样式、结构、公式** 有精细化控制需求时使用。配合 Pandas 可以实现强大的报表自动化。
