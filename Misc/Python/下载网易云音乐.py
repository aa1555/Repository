import requests
import re
import os

# 歌单的URL
url = 'https://music.163.com/discover/toplist?id=3778678'

# 请求头部，模拟浏览器访问
headers = {
    # ...在这里添加适当的头部信息...
}

# 向URL发送GET请求
res = requests.get(url, headers=headers)

# 使用正则表达式找到所有歌曲的ID和标题
# re.findall(pattern, string, flags=0)函数返回一个列表，列表中包含所有匹配的子串。
ids = re.findall(r'href="/song\?id=(\d*?)">(.+?)</a>', res.text)

# 创建保存歌曲的目录
# 这两行代码确保了 d:/files/temp/ 这个目录存在，如果不存在，就会创建它，而且如果目录已经存在，代码不会因为这个而停止执行或抛出错误。这是非常有用的，因为在你想要确保目录存在的情况下，你不需要先检查它是否存在，然后才决定是否创建它。
output_directory = 'd:/files/temp/'
os.makedirs(output_directory, exist_ok=True)

# 下载每首歌曲
for song_id, song_title in ids:
    # 构造歌曲的URL
    song_url = f'http://music.163.com/song/media/outer/url?id={song_id}.mp3'
    
    # 向歌曲URL发送GET请求
    song_res = requests.get(song_url, headers=headers)
    
    # 定义歌曲保存的路径
    path = output_directory + f'{song_title}.mp3'
    
    # 将歌曲内容写入文件
    with open(path, 'wb') as f:
        f.write(song_res.content)
    
    print(f'已下载 {song_title}')

print('所有歌曲下载完成。')
