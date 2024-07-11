import requests
from lxml import etree

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

# 设置目标网页的URL
url = 'https://www.mn52.com/fj/11408.html'

# 发送GET请求
response = requests.get(url, headers=headers)

# 解析HTML响应
html = etree.HTML(response.text)

# 使用XPath获取图片URL
image_urls = html.xpath('//div[@id="originalpic"]/img/@src')

# 遍历图片URL列表，下载图片
for image_url in image_urls:
    # 拼接完整的图片URL
    full_image_url = 'https://www.mn52.com' + image_url
    # 发送GET请求下载图片
    image_response = requests.get(full_image_url, headers=headers)
    
    # 提取图片文件名
    # str.split()方法，用于将字符串分割成一个列表。
    # split('/')方法会在每个斜杠（/）处分割这个字符串，并返回一个列表。
    # [-1]表示索引列表的最后一个元素
    image_filename = image_url.split('/')[-1]
    
    # 保存图片到本地
    with open(fr'C:\Users\Administrator\Desktop\新建文件夹\{image_filename}', 'wb') as f:
        f.write(image_response.content)

    # 打印图片信息
    print(image_filename,full_image_url)
    
print('完成')