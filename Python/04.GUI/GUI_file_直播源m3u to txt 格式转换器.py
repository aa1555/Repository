import re
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import logging
import threading
from pathlib import Path

class M3U8ParserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("M3U8/M3U to TXT 解析转换器")
        self.root.geometry("800x600")
        
        # 初始化变量
        self.input_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.processing = False
        
        # 创建界面组件
        self.create_widgets()
        
        # 配置日志到文本框
        self.setup_logging()

    def setup_logging(self):
        self.log_handler = TextHandler(self.log_text)
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[self.log_handler]
        )

    def create_widgets(self):
        # 主容器
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 输入文件选择
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(input_frame, text="M3U8/M3U输入文件:").pack(side=tk.LEFT)
        ttk.Entry(input_frame, textvariable=self.input_path, width=50).pack(side=tk.LEFT, padx=5)
        ttk.Button(input_frame, text="浏览...", command=self.browse_input).pack(side=tk.LEFT)

        # 输出文件选择
        output_frame = ttk.Frame(main_frame)
        output_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(output_frame, text="             TXT输出文件:").pack(side=tk.LEFT)
        ttk.Entry(output_frame, textvariable=self.output_path, width=50).pack(side=tk.LEFT, padx=5)
        ttk.Button(output_frame, text="浏览...", command=self.browse_output).pack(side=tk.LEFT)

        # 控制按钮
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=10)
        
        self.convert_btn = ttk.Button(btn_frame, text="开始转换", command=self.start_conversion)
        self.convert_btn.pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="退出", command=self.root.quit).pack(side=tk.LEFT)

        # 日志显示
        log_frame = ttk.Frame(main_frame)
        log_frame.pack(fill=tk.BOTH, expand=True)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, state='disabled', height=15)
        self.log_text.pack(fill=tk.BOTH, expand=True)

        # 状态栏
        self.status_var = tk.StringVar()
        ttk.Label(main_frame, textvariable=self.status_var).pack(side=tk.BOTTOM, fill=tk.X)

    def browse_input(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("M3U/M3U8 files", "*.m3u *.m3u8"), ("All files", "*.*")]
        )
        if file_path:
            self.input_path.set(file_path)
            # 自动生成输出路径
            output_path = Path(file_path).with_suffix('.txt')
            self.output_path.set(str(output_path))

    def browse_output(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            self.output_path.set(file_path)

    def start_conversion(self):
        if self.processing:
            return
        
        input_file = self.input_path.get()
        output_file = self.output_path.get()

        if not input_file:
            messagebox.showerror("错误", "请先选择输入文件")
            return

        if not Path(input_file).exists():
            messagebox.showerror("错误", "输入文件不存在")
            return

        if not output_file:
            messagebox.showerror("错误", "请指定输出文件路径")
            return

        self.processing = True
        self.status_var.set("处理中...")
        self.convert_btn.config(state=tk.DISABLED)

        # 使用线程处理转换
        threading.Thread(
            target=self.run_conversion,
            args=(input_file, output_file),
            daemon=True
        ).start()

    def run_conversion(self, input_file, output_file):
        try:
            success = parse_m3u8(input_file, output_file)
            if success:
                self.status_var.set(f"转换完成！文件已保存到：{output_file}")
                messagebox.showinfo("完成", "转换成功！")
            else:
                self.status_var.set("转换失败")
        except Exception as e:
            logging.error(f"发生未预期错误: {str(e)}")
            messagebox.showerror("错误", f"处理过程中出现错误:\n{str(e)}")
        finally:
            self.processing = False
            self.root.after(0, lambda: self.convert_btn.config(state=tk.NORMAL))

def parse_m3u8(input_file, output_file):
    # 存储分类和频道信息的字典
    categories = {}
    current_category = None
    current_channel = None
    processed_channels = 0
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        logging.info(f"开始解析文件: {input_file}")
        
        for line in lines:
            line = line.strip()
            
            # 跳过空行和#EXTM3U行
            if not line or line.startswith('#EXTM3U'):
                continue
                
            # 解析频道信息行
            if line.startswith('#EXTINF'):
                # 使用正则表达式提取频道名称和分类
                match = re.search(r'tvg-name="([^"]+)".*group-title="([^"]+)"', line)
                if match:
                    current_channel = match.group(1)
                    category = match.group(2)
                    
                    # 初始化分类字典
                    if category not in categories:
                        categories[category] = []
                        
                    current_category = category
                else:
                    logging.warning(f"无法解析的行: {line}")
                    
            # 处理URL行
            elif current_channel and current_category:
                # 添加频道和URL到对应分类
                categories[current_category].append((current_channel, line))
                processed_channels += 1
                current_channel = None
        
        logging.info(f"共找到 {len(categories)} 个分类，{processed_channels} 个频道")
        
        # 写入输出文件
        with open(output_file, 'w', encoding='utf-8') as f:
            for category, channels in categories.items():
                # 写入分类标题
                f.write(f"{category},#genre#\n")
                
                # 写入频道信息
                for channel, url in channels:
                    f.write(f"{channel},{url}\n")
                
                # 添加空行分隔不同分类
                f.write("\n")
        
        logging.info(f"成功写入输出文件: {output_file}")
        return True
        
    except Exception as e:
        logging.error(f"处理文件时出错: {str(e)}")
        raise

class TextHandler(logging.Handler):
    """将日志输出重定向到ScrolledText组件"""
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget
        
    def emit(self, record):
        msg = self.format(record)
        self.text_widget.configure(state='normal')
        self.text_widget.insert(tk.END, msg + '\n')
        self.text_widget.configure(state='disabled')
        self.text_widget.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = M3U8ParserApp(root)
    root.mainloop()