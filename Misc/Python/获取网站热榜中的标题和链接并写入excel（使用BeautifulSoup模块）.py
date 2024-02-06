# 导入所需的模块
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# 微博热榜的网址
url = "https://tophub.today/n/KqndgxeLl9"

# 设置User-Agent字符串来模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

# 发送请求获取网页内容
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'  # 确保中文字符可以正确解析

# 使用BeautifulSoup解析网页
soup = BeautifulSoup(response.text, 'html.parser')

# 提取标题和链接
# 使用CSS选择器来选择每个tr元素
tr_elements = soup.select('tr:has(td:nth-child(2) a)') #选择第二个td中含有<a>元素的tr元素

# 创建Excel工作簿
wb = Workbook()
ws = wb.active

# 将标题和链接写入Excel
ws.append(['标题', '链接'])
for tr_element in tr_elements:
    a_element = tr_element.select_one('td:nth-child(2) a')  # 选择td中的a元素
    title = a_element.get_text() if a_element else ''  # 获取a元素中的文本
    link = a_element['href'] if a_element else ''  # 获取a元素的href属性
    ws.append([title, link])

# 保存Excel文件
excel_file_path = r'C:\Users\Administrator\Desktop\新建文件夹\Weibo_Hot.xlsx'  # 保持路径和文件名
wb.save(excel_file_path)
print('完成')
