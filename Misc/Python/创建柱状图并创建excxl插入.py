import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import Workbook
from openpyxl.drawing.image import Image
# 数据准备
data = {
    '类别': ['收入', '成本', '运营费用', '税金', '净利润'],
    '金额': [100000, 70000, 15000, 5000, 20000]
}
df = pd.DataFrame(data)
# 创建柱状图
plt.figure(figsize=(10, 6))
plt.bar(df['类别'], df['金额'], color='skyblue')
plt.xlabel('类别')
plt.ylabel('金额')
plt.title('利润表柱状图')
plt.xticks(rotation=45)
plt.tight_layout()
# 保存柱状图为图片
bar = 'bar_chart.png'
plt.savefig(bar)
# 指定Excel文件保存的路径
excel = 'E:\\下载\\示例.xlsx'
# 创建Excel写入器
with pd.ExcelWriter(excel, engine='openpyxl') as writer:
    # 将数据写入Excel
    df.to_excel(writer, index=False, sheet_name='利润表')
    
    # 加载工作簿和工作表
    workbook  = writer.book
    worksheet = writer.sheets['利润表']
    
    # 插入图片到Excel工作表
    img = Image(bar)
    worksheet.add_image(img, 'A8')  # 假设从A8单元格开始插入图片
# 清除matplotlib图表，避免重复插入
plt.clf()