import os
import logging
from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext

class LogHandler(logging.Handler):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget
        
    def emit(self, record):
        msg = self.format(record)
        self.text_widget.insert(tk.END, msg + '\n')
        self.text_widget.see(tk.END)

class M3U8ConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("M3U8 转换器")
        self.root.geometry("600x400")
        
        # 创建主框架
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 文件选择部分
        self.input_path = tk.StringVar()
        ttk.Label(self.main_frame, text="输入文件:").grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(self.main_frame, textvariable=self.input_path, width=50).grid(row=0, column=1, padx=5)
        ttk.Button(self.main_frame, text="浏览", command=self.select_input_file).grid(row=0, column=2)
        
        # 转换按钮
        ttk.Button(self.main_frame, text="开始转换", command=self.start_conversion).grid(row=1, column=0, columnspan=3, pady=10)
        
        # 日志显示区域
        self.log_area = scrolledtext.ScrolledText(self.main_frame, height=15, width=70)
        self.log_area.grid(row=2, column=0, columnspan=3, pady=5)
        
        # 设置日志处理
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        log_handler = LogHandler(self.log_area)
        log_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logging.getLogger().addHandler(log_handler)

    def select_input_file(self):
        filename = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
            self.input_path.set(filename)

    def start_conversion(self):
        input_file = self.input_path.get()
        if not input_file:
            logging.error("请选择输入文件")
            return
            
        input_path = Path(input_file)
        output_path = Path(input_path.parent) / f"{input_path.stem}.m3u8"
        
        if convert_to_m3u8(str(input_path), str(output_path)):
            logging.info(f"文件已保存到: {output_path}")
        else:
            logging.error("转换失败")

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def convert_to_m3u8(input_file, output_file):
    current_group_title = None
    processed_count = 0
    error_count = 0
    
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, \
             open(output_file, 'w', encoding='utf-8') as outfile:
            # 写入M3U8文件头
            outfile.write('#EXTM3U\n')
            
            for line_num, line in enumerate(infile, 1):
                line = line.strip()
                if not line:
                    continue
                    
                # 检查是否是分组标题行
                if line.endswith(",#genre#"):
                    current_group_title = line[:-7].strip()
                    continue
                    
                # 检查是否是频道行
                if line and current_group_title:
                    try:
                        # 使用rsplit从右侧分割，最多分割一次
                        parts = line.rsplit(',', 1)
                        if len(parts) != 2:
                            raise ValueError("格式错误：需要频道名和URL，用逗号分隔")
                            
                        channel_name, url = parts
                        channel_name = channel_name.strip()
                        url = url.strip()
                        
                        if not url.startswith(('http://', 'https://', 'rtmp://', 'rtsp://')):
                            logging.warning(f"第 {line_num} 行: URL格式可能不正确: {url}")
                        
                        # 构造完整的M3U8格式的字符串
                        m3u8_line = (
                            f'#EXTINF:-1 tvg-id="{channel_name}" '
                            f'tvg-name="{channel_name}" '
                            f'group-title="{current_group_title.replace(",", "")}",{channel_name}\n'
                            f'{url}\n'
                        )
                        outfile.write(m3u8_line)
                        processed_count += 1
                        
                    except Exception as e:
                        error_count += 1
                        logging.error(f"处理第 {line_num} 行时出错: {line}\n错误: {str(e)}")
                        
    except IOError as e:
        logging.error(f"文件操作错误: {str(e)}")
        return False
        
    logging.info(f"转换完成: 成功处理 {processed_count} 个频道，失败 {error_count} 个")
    return True

def main():
    root = tk.Tk()
    app = M3U8ConverterGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()