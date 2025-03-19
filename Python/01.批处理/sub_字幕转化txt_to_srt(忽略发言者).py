import re

def format_subtitle(input_text):
    entries = []
    lines = input_text.strip().split('\n')
    current_entry = {}
    time_pattern = re.compile(r'(\d{2}:\d{2}:\d{2}:\d{2})\s*-\s*(\d{2}:\d{2}:\d{2}:\d{2})')
    speaker_pattern = re.compile(r'^发言者\s+\d+$')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        time_match = time_pattern.match(line)
        if time_match:
            if current_entry:
                entries.append(current_entry)
            start, end = time_match.groups()
            start = ":".join(start.split(':')[:3]) + "," + start.split(':')[3]
            end = ":".join(end.split(':')[:3]) + "," + end.split(':')[3]
            current_entry = {
                'time': f"{start} --> {end}",
                'text': []
            }
        else:
            if speaker_pattern.match(line):
                continue
            if current_entry:
                current_entry['text'].append(line)
    
    if current_entry:
        entries.append(current_entry)
    
    output = []
    for index, entry in enumerate(entries, 1):
        output.append(str(index))
        output.append(entry['time'])
        output.append('\n'.join(entry['text']))  # 保留原始换行
        output.append('')
    
    return '\n'.join(output).strip()

def process_file(input_file, output_file):
    """文件处理函数"""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        formatted = format_subtitle(content)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(formatted)
        
        print(f"文件处理成功！输出文件已保存至：{output_file}")
    
    except Exception as e:
        print(f"处理过程中发生错误：{str(e)}")

if __name__ == "__main__":
    input_path = r"C:\Users\aa155\Desktop\00.txt"
    output_path = r"C:\Users\aa155\Desktop\00.srt"
    process_file(input_path, output_path)



# 举例：

# 原数据：

# 00:00:15:29 - 00:00:30:01
# 发言者 2
# 想在开始拍摄前问妳一些问题。可以吗？好的，请从名字开始告诉我。是相川小姐。不好意思，相川小姐。现在几岁呢？

# 00:00:30:08 - 00:00:31:21
# 发言者 1
# 现在24岁。

# 00:00:31:24 - 00:00:34:26
# 发言者 3
# 24岁25岁。

# 转化后：

# 1
# 00:00:15,29 --> 00:00:30,01
# 想在开始拍摄前问妳一些问题。可以吗？好的，请从名字开始告诉我。是相川小姐。不好意思，相川小姐。现在几岁呢？

# 2
# 00:00:30,08 --> 00:00:31,21
# 现在24岁。

# 3
# 00:00:31,24 --> 00:00:34,26
# 24岁25岁。