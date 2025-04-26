import re
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import logging
import threading
from pathlib import Path

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

class M3U8Converter:
    def __init__(self, root):
        self.root = root
        self.root.title("txt to m3u8 格式转换器")
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
        
        ttk.Label(input_frame, text="TXT输入文件:").pack(side=tk.LEFT)
        ttk.Entry(input_frame, textvariable=self.input_path, width=50).pack(side=tk.LEFT, padx=5)
        ttk.Button(input_frame, text="浏览...", command=self.browse_input).pack(side=tk.LEFT)

        # 输出文件选择
        output_frame = ttk.Frame(main_frame)
        output_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(output_frame, text="M3U8输出文件:").pack(side=tk.LEFT)
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
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            self.input_path.set(file_path)
            # 自动生成输出路径
            output_path = Path(file_path).with_suffix('.m3u8')
            self.output_path.set(str(output_path))

    def browse_output(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".m3u8",
            filetypes=[("M3U8 files", "*.m3u8"), ("All files", "*.*")]
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
            success = self.convert_to_m3u8(input_file, output_file)
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

    def convert_to_m3u8(self, input_file, output_file):
        current_group_title = None
        processed_channels = 0
        
        try:
            with open(input_file, 'r', encoding='utf-8') as infile:
                lines = infile.readlines()
            
            logging.info(f"开始解析文件: {input_file}")
            
            with open(output_file, 'w', encoding='utf-8') as outfile:
                outfile.write("#EXTM3U\n")  # 添加M3U8头部
                
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                        
                    if line.endswith(",#genre#"):
                        current_group_title = line[:-7]
                        logging.info(f"找到分类: {current_group_title}")
                        continue
                        
                    if line and current_group_title:
                        try:
                            parts = line.split(',', 1)
                            if len(parts) != 2:
                                logging.warning(f"跳过格式不正确的行: {line}")
                                continue
                                
                            channel_name, url = parts
                            channel_name = channel_name.strip()
                            m3u8_line = (
                                f'#EXTINF:-1 tvg-name="{channel_name}" '
                                f'group-title="{current_group_title.replace(",", "")}",{channel_name}\n'
                                f'{url}\n'
                            )
                            outfile.write(m3u8_line)
                            processed_channels += 1
                        except Exception as e:
                            logging.warning(f"处理行时出错: {line}. 错误: {e}")
            
            logging.info(f"转换完成，共处理 {processed_channels} 个频道")
            return True
            
        except IOError as e:
            logging.error(f"文件操作错误: {e}")
            raise Exception(f"文件操作错误: {e}")
        except Exception as e:
            logging.error(f"处理文件时出错: {str(e)}")
            raise

def main():
    root = tk.Tk()
    app = M3U8Converter(root)
    root.mainloop()

if __name__ == "__main__":
    main()