import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class FileRenamerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("文件重命名工具")
        self.root.geometry("900x700")  # 进一步扩大窗口
        
        # 设置窗口最小尺寸
        self.root.minsize(800, 600)
        
        # 创建主框架
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 文件夹选择部分
        self.folder_frame = ttk.LabelFrame(self.main_frame, text="选择文件夹", padding="15")
        self.folder_frame.pack(fill=tk.X, pady=10)
        
        self.folder_path = tk.StringVar()
        self.folder_entry = ttk.Entry(self.folder_frame, textvariable=self.folder_path)
        self.folder_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.browse_button = ttk.Button(self.folder_frame, text="浏览文件夹...", command=self.browse_folder)
        self.browse_button.pack(side=tk.RIGHT)
        
        # 重命名选项部分
        self.options_frame = ttk.LabelFrame(self.main_frame, text="重命名选项", padding="15")
        self.options_frame.pack(fill=tk.X, pady=15)
        
        # 删除文本选项
        ttk.Label(self.options_frame, text="要删除的文本:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.text_to_remove = tk.StringVar()
        self.text_entry = ttk.Entry(self.options_frame, textvariable=self.text_to_remove, width=30)
        self.text_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        
        # 添加前缀选项
        ttk.Label(self.options_frame, text="添加前缀:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.prefix_text = tk.StringVar()
        self.prefix_entry = ttk.Entry(self.options_frame, textvariable=self.prefix_text, width=30)
        self.prefix_entry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        
        # 添加后缀选项
        ttk.Label(self.options_frame, text="添加后缀:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.suffix_text = tk.StringVar()
        self.suffix_entry = ttk.Entry(self.options_frame, textvariable=self.suffix_text, width=30)
        self.suffix_entry.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        
        # 文件筛选选项
        ttk.Label(self.options_frame, text="文件扩展名筛选(可选):").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.filter_ext = tk.StringVar()
        self.filter_entry = ttk.Entry(self.options_frame, textvariable=self.filter_ext, width=30)
        self.filter_entry.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)
        self.filter_entry.insert(0, "*")  # 默认显示所有文件
        
        # 日志部分
        self.log_frame = ttk.LabelFrame(self.main_frame, text="操作日志", padding="15")
        self.log_frame.pack(fill=tk.BOTH, expand=True, pady=15)
        
        self.log_text = tk.Text(self.log_frame, height=20, wrap=tk.WORD)
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
        # 滚动条
        self.scrollbar = ttk.Scrollbar(self.log_text)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.log_text.yview)
        
        # 操作按钮
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(fill=tk.X, pady=20)
        
        # 按钮样式
        button_style = ttk.Style()
        button_style.configure('Large.TButton', font=('Arial', 10, 'bold'), padding=8)
        
        # 预览按钮
        self.preview_button = ttk.Button(
            self.button_frame, 
            text="预览修改", 
            command=self.preview_changes,
            style='Large.TButton'
        )
        self.preview_button.pack(side=tk.LEFT, padx=15, ipadx=25)
        
        # 重命名按钮
        self.rename_button = ttk.Button(
            self.button_frame, 
            text="执行重命名", 
            command=self.rename_files,
            style='Large.TButton'
        )
        self.rename_button.pack(side=tk.LEFT, padx=15, ipadx=25)
        
        # 清空日志按钮
        self.clear_button = ttk.Button(
            self.button_frame, 
            text="清空日志", 
            command=self.clear_log,
            style='Large.TButton'
        )
        self.clear_button.pack(side=tk.LEFT, padx=15, ipadx=25)
        
        # 退出按钮
        self.exit_button = ttk.Button(
            self.button_frame, 
            text="退出程序", 
            command=self.root.quit,
            style='Large.TButton'
        )
        self.exit_button.pack(side=tk.RIGHT, padx=15, ipadx=25)
    
    def browse_folder(self):
        """打开文件夹选择对话框"""
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path.set(folder_selected)
    
    def preview_changes(self):
        """预览将要进行的修改"""
        directory = self.folder_path.get()
        
        if not directory:
            messagebox.showerror("错误", "请先选择文件夹！")
            return
        
        try:
            self.log("\n=== 预览修改 ===")
            file_count = 0
            for filename in os.listdir(directory):
                old_path = os.path.join(directory, filename)
                
                if not os.path.isfile(old_path):
                    continue
                
                # 检查文件扩展名筛选
                ext_filter = self.filter_ext.get().strip()
                if ext_filter != "*":
                    file_ext = os.path.splitext(filename)[1].lower()
                    if not file_ext or file_ext != f".{ext_filter.lower().lstrip('.')}":
                        continue
                
                new_name = self.generate_new_name(filename)
                
                if new_name != filename:
                    self.log(f"将重命名: {filename} -> {new_name}")
                    file_count += 1
            
            if file_count == 0:
                self.log("没有需要重命名的文件")
            else:
                self.log(f"\n共发现 {file_count} 个文件需要重命名")
        
        except Exception as e:
            messagebox.showerror("错误", f"预览时发生错误: {str(e)}")
            self.log(f"错误: {str(e)}")
    
    def generate_new_name(self, filename):
        """生成新的文件名"""
        new_name = filename
        
        # 删除指定文本
        text_to_remove = self.text_to_remove.get().strip()
        if text_to_remove:
            new_name = new_name.replace(text_to_remove, "")
        
        # 添加前缀
        prefix = self.prefix_text.get().strip()
        if prefix:
            new_name = prefix + new_name
        
        # 添加后缀（在扩展名之前）
        suffix = self.suffix_text.get().strip()
        if suffix:
            name_part, ext_part = os.path.splitext(new_name)
            new_name = f"{name_part}{suffix}{ext_part}"
        
        return new_name
    
    def rename_files(self):
        """执行文件重命名操作"""
        directory = self.folder_path.get()
        
        if not directory:
            messagebox.showerror("错误", "请先选择文件夹！")
            return
        
        try:
            renamed_count = 0
            for filename in os.listdir(directory):
                old_path = os.path.join(directory, filename)
                
                if not os.path.isfile(old_path):
                    continue
                
                # 检查文件扩展名筛选
                ext_filter = self.filter_ext.get().strip()
                if ext_filter != "*":
                    file_ext = os.path.splitext(filename)[1].lower()
                    if not file_ext or file_ext != f".{ext_filter.lower().lstrip('.')}":
                        continue
                
                new_name = self.generate_new_name(filename)
                
                if new_name != filename:
                    new_path = os.path.join(directory, new_name)
                    
                    # 检查新文件名是否已存在
                    if os.path.exists(new_path):
                        self.log(f"警告: 跳过 {filename} -> {new_name} (目标文件已存在)")
                        continue
                    
                    os.rename(old_path, new_path)
                    self.log(f"重命名: {filename} -> {new_name}")
                    renamed_count += 1
            
            self.log(f"\n操作完成！共重命名了 {renamed_count} 个文件。")
            messagebox.showinfo("完成", f"文件重命名完成！共重命名了 {renamed_count} 个文件。")
        
        except Exception as e:
            messagebox.showerror("错误", f"发生错误: {str(e)}")
            self.log(f"错误: {str(e)}")
    
    def log(self, message):
        """向日志区域添加消息"""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)  # 自动滚动到底部
        self.log_text.config(state=tk.DISABLED)
    
    def clear_log(self):
        """清空日志区域"""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete(1.0, tk.END)
        self.log_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileRenamerApp(root)
    root.mainloop()