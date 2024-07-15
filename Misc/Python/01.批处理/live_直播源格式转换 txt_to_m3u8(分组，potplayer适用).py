# 定义一个函数，将简化的格式转换为完整的M3U8格式
def convert_to_m3u8(input_file, output_file):
    current_group_title = None
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            line = line.strip()
            # 检查是否是分组标题行
            if line.endswith(",#genre#"):
                current_group_title = line[:-7]
                continue
            # 检查是否是频道行
            if line and current_group_title:
                try:
                    # 使用多个逗号分割，并且最多分割成两部分
                    parts = line.split(',')
                    if len(parts) != 2:
                        raise ValueError("Line format is incorrect.")
                    channel_name, url = parts
                    channel_name = channel_name.strip()
                    # 构造完整的M3U8格式的字符串
                    m3u8_line = (
                        f'#EXTINF:-1 tvg-name="{channel_name}" '
                        f'group-title="{current_group_title.replace(",", "")}",{channel_name}\n'
                        f'{url}\n'
                    )
                    outfile.write(m3u8_line)
                except ValueError as e:
                    print(f"Error processing line: {line}. Error: {e}")

# 替换以下路径为您的文件路径
input_txt_file = r"C:\Users\aa155\Desktop\示例.txt"  # 输入文件路径
output_m3u8_file = r"C:\Users\aa155\Desktop\示例.m3u8"  # 输出文件路径

# 调用函数进行转换
convert_to_m3u8(input_txt_file, output_m3u8_file)
