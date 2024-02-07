import requests
from lxml import etree
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

# 使用lxml解析网页（因为BeautifulSoup不支持XPath）
tree = etree.HTML(response.text)

# 提取标题和链接
# chrome复制的xpath路径：//*[@id="page"]/div[2]/div[2]/div[1]/div[2]/div/div[1]/table/tbody/tr[1]/td[2]/a
# 使用XPath路径来选择每个tr元素。因为标题和链接是被包含在每一个tr元素下的。
tr_elements = tree.xpath('//*[@id="page"]/div[2]/div[2]/div[1]/div[2]/div/div[1]/table/tbody/tr')

# 创建Excel工作簿
wb = Workbook()
ws = wb.active

# 将标题和链接写入Excel
ws.append(['标题', '链接'])
for tr_element in tr_elements:
    title_element = tr_element.xpath('td[2]/a')[0]  # 对每个tr进行迭代，并进一步提取每个tr中的第二个td中的a元素
    title = title_element.xpath('text()')[0]  # 获取a元素中的文本
    link = title_element.xpath('@href')[0]  # 获取a元素的href属性
    ws.append([title, link])

# 保存Excel文件
excel_file_path = r'C:\Users\Administrator\Desktop\新建文件夹\Weibo_Hot.xlsx'  # 保持路径和文件名
wb.save(excel_file_path)
print('完成')
