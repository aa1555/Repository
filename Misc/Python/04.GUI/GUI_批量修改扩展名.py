import os
import tkinter as tk
from tkinter import filedialog, messagebox

def batch_rename():
    directory = directory_entry.get()
    old_extension = old_extension_entry.get()
    new_extension = new_extension_entry.get()

    # 检查输入是否完整
    if not directory or not old_extension or not new_extension:
        messagebox.showerror("错误", "请填写所有字段。")
        return

    # 检查旧扩展名和新扩展名是否以点号开头
    if not old_extension.startswith('.'):
        old_extension = '.' + old_extension
    if not new_extension.startswith('.'):
        new_extension = '.' + new_extension

    # 重命名文件
    renamed_files_count = 0
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath) and filename.endswith(old_extension):
            new_filename = filename[:-len(old_extension)] + new_extension
            new_filepath = os.path.join(directory, new_filename)
            os.rename(filepath, new_filepath)
            print(f"已重命名 '{filename}' 为 '{new_filename}'")
            renamed_files_count += 1

    messagebox.showinfo("完成", f"成功重命名了 {renamed_files_count} 个文件。")

# 创建主窗口
root = tk.Tk()
root.title("批量重命名文件")

# 创建输入框和标签
tk.Label(root, text="选择文件夹:").grid(row=0, column=0, padx=10, pady=10)
directory_entry = tk.Entry(root, width=50)
directory_entry.grid(row=0, column=1)
tk.Button(root, text="浏览", command=lambda: directory_entry.insert(0, filedialog.askdirectory())).grid(row=0, column=2)

tk.Label(root, text="旧扩展名:").grid(row=1, column=0, padx=10, pady=10)
old_extension_entry = tk.Entry(root)
old_extension_entry.grid(row=1, column=1)

tk.Label(root, text="新扩展名:").grid(row=2, column=0, padx=10, pady=10)
new_extension_entry = tk.Entry(root)
new_extension_entry.grid(row=2, column=1)

# 创建重命名按钮
tk.Button(root, text="批量重命名", command=batch_rename).grid(row=3, column=1, pady=10)

# 启动主循环
root.mainloop()
