import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

class M3U8Converter:
    def __init__(self, root):
        self.root = root
        self.root.title("直播源格式转换器")
        self.root.geometry("600x300")
        
        # 创建主框架
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 输入文件选择
        ttk.Label(self.main_frame, text="输入文件:").grid(row=0, column=0, sticky=tk.W)
        self.input_path = tk.StringVar()
        self.input_entry = ttk.Entry(self.main_frame, textvariable=self.input_path, width=50)
        self.input_entry.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(self.main_frame, text="浏览", command=self.select_input_file).grid(row=0, column=2)
        
        # 输出文件选择
        ttk.Label(self.main_frame, text="输出文件:").grid(row=1, column=0, sticky=tk.W)
        self.output_path = tk.StringVar()
        self.output_entry = ttk.Entry(self.main_frame, textvariable=self.output_path, width=50)
        self.output_entry.grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(self.main_frame, text="浏览", command=self.select_output_file).grid(row=1, column=2)
        
        # 转换按钮
        ttk.Button(self.main_frame, text="开始转换", command=self.start_conversion).grid(row=2, column=1, pady=20)
        
        # 进度条
        self.progress = ttk.Progressbar(self.main_frame, length=400, mode='indeterminate')
        self.progress.grid(row=3, column=0, columnspan=3, pady=10)

    def select_input_file(self):
        filename = filedialog.askopenfilename(
            title="选择输入文件",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
            self.input_path.set(filename)
            # 自动设置输出文件路径
            output_name = os.path.splitext(os.path.basename(filename))[0] + ".m3u8"
            self.output_path.set(os.path.join(os.path.expanduser("~"), "Desktop", output_name))

    def select_output_file(self):
        filename = filedialog.asksaveasfilename(
            title="选择保存位置",
            defaultextension=".m3u8",
            filetypes=[("M3U8 files", "*.m3u8"), ("All files", "*.*")]
        )
        if filename:
            self.output_path.set(filename)

    def start_conversion(self):
        input_file = self.input_path.get()
        output_file = self.output_path.get()
        
        if not input_file or not output_file:
            messagebox.showerror("错误", "请选择输入和输出文件!")
            return
            
        self.progress.start()
        try:
            self.convert_to_m3u8(input_file, output_file)
            messagebox.showinfo("成功", "转换完成！")
        except Exception as e:
            messagebox.showerror("错误", f"转换过程中出现错误：{str(e)}")
        finally:
            self.progress.stop()

    def convert_to_m3u8(self, input_file, output_file):
        current_group_title = None
        try:
            with open(input_file, 'r', encoding='utf-8') as infile, \
                 open(output_file, 'w', encoding='utf-8') as outfile:
                outfile.write("#EXTM3U\n")  # 添加M3U8头部
                for line in infile:
                    line = line.strip()
                    if line.endswith(",#genre#"):
                        current_group_title = line[:-7]
                        continue
                    if line and current_group_title:
                        try:
                            parts = line.split(',', 1)
                            if len(parts) != 2:
                                raise ValueError("格式不正确")
                            channel_name, url = parts
                            channel_name = channel_name.strip()
                            m3u8_line = (
                                f'#EXTINF:-1 tvg-name="{channel_name}" '
                                f'group-title="{current_group_title.replace(",", "")}",{channel_name}\n'
                                f'{url}\n'
                            )
                            outfile.write(m3u8_line)
                        except ValueError as e:
                            print(f"处理行时出错: {line}. 错误: {e}")
        except IOError as e:
            raise Exception(f"文件操作错误: {e}")

def main():
    root = tk.Tk()
    app = M3U8Converter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
