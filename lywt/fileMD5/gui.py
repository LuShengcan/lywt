import tkinter as tk
from tkinter import ttk
import windnd
from tkinter import scrolledtext
from .cli import md5


class FileMD5(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.creat_window()
        self.create_widgets()
        self.grid_widgets()
        windnd.hook_dropfiles(self.text_10, func=self.drag_files)

    def creat_window(self):
        self.title('文件MD5计算')
        self.window_width = 800
        self.window_height = 200
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.window_width) // 2
        y = (screen_height - self.window_height) // 2
        self.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")

    def create_widgets(self):
        # row 0
        self.label_00 = tk.Label(self, text='拖放文件：')
        self.label_01 = ttk.Label(self, text='MD5值：')

        # row 1
        self.text_10 = scrolledtext.ScrolledText(self, width=50, height=10)
        self.text_11 = scrolledtext.ScrolledText(self, width=35, height=10)

    def grid_widgets(self):
        # row 0
        self.label_00.grid(row=0, column=0, sticky='w')
        self.label_01.grid(row=0, column=1, sticky='w')

        # row 1
        self.text_10.grid(row=1, column=0)
        self.text_11.grid(row=1, column=1)

    def drag_files(self, file_paths):
        for path in file_paths:
            try:
                path: bytes = path.decode('utf-8')
            except UnicodeDecodeError:
                path: bytes = path.decode('gbk')
            finally:
                self.text_10.insert(tk.END, path + '\n')
                self.text_11.insert(tk.END, md5(path) + '\n')
