import requests
from lxml import etree

# 设置请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0 Safari/537.36"
}

# 目标URL
url = 'https://movie.douban.com/top250'

# 发送GET请求
response = requests.get(url, headers=headers)

# 解析HTML内容
tree = etree.HTML(response.text)

# 提取图片元素
imgs = tree.xpath('//img[@width="100"]')

# 遍历图片元素
for img in imgs:
    # 获取图片的alt属性和src属性，alt是图片名，src是图片地址。
    alt_text = img.get('alt')
    img_url = img.get('src')

    # 打印图片信息
    print(alt_text, img_url)

    # 下载图片
    img_response = requests.get(img_url, headers=headers)

    # 保存图片到文件
    with open(f"{alt_text}.jpg", 'wb') as file:
        file.write(img_response.content)
