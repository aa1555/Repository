import os
import tkinter as tk
from tkinter import filedialog, messagebox

def rename_files():
    directory = directory_entry.get()
    prefix_to_remove = prefix_entry.get()

    # 获取当前目录下所有文件和目录列表
    files_and_dirs = os.listdir(directory)

    # 遍历文件和目录列表
    for item in files_and_dirs:
        # 检查是否是文件
        if os.path.isfile(os.path.join(directory, item)):
            # 检查文件名是否以前缀开头
            if item.startswith(prefix_to_remove):
                # 构造新的文件名（移除前缀）
                new_name = item[len(prefix_to_remove):]
                # 重命名文件
                os.rename(os.path.join(directory, item), os.path.join(directory, new_name))
                print(f'文件"{item}"已重命名为"{new_name}"')
    messagebox.showinfo("完成", "所有文件已删除前缀。")

# 创建主窗口
root = tk.Tk()
root.title("删除文件名前缀")

# 创建输入框和标签
tk.Label(root, text="文件夹路径:").grid(row=0, column=0)
directory_entry = tk.Entry(root, width=50)
directory_entry.grid(row=0, column=1)

tk.Label(root, text="删除前缀:").grid(row=1, column=0)
prefix_entry = tk.Entry(root, width=50)
prefix_entry.grid(row=1, column=1)

# 创建选择文件夹按钮
def choose_directory():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, directory)

choose_button = tk.Button(root, text="选择文件夹", command=choose_directory)
choose_button.grid(row=0, column=2)

# 创建重命名按钮
rename_button = tk.Button(root, text="确定", command=rename_files)
rename_button.grid(row=2, column=1)

# 运行主循环
root.mainloop()