import tkinter as tk
from tkinter import ttk
import windnd
from tkinter import scrolledtext
from .fileMD5_cli import md5

# to do:增加鼠标悬停预览


class FileMD5(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # 控件
        f0 = ttk.Frame(self)
        f0.pack(side=tk.TOP, pady=10)

        tk.Label(f0, text='拖放文件：').grid(row=0, column=0, sticky='w')

        ttk.Label(f0, text='MD5值：').grid(row=0, column=1, sticky='w')

        self.file_list = scrolledtext.ScrolledText(f0, width=35, height=10, wrap='none')
        self.file_list.grid(row=1, column=0)

        self.md5value = scrolledtext.ScrolledText(f0, width=33, height=10)
        self.md5value.grid(row=1, column=1)

        windnd.hook_dropfiles(self.file_list, func=self.drag_files)

    def drag_files(self, file_paths):
        for path in file_paths:
            try:
                path: bytes = path.decode('utf-8')
            except UnicodeDecodeError:
                path: bytes = path.decode('gbk')
            finally:
                self.file_list.insert(tk.END, path + '\n')
                self.md5value.insert(tk.END, md5(path) + '\n')
