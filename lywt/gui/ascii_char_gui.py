import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from ..cli.ascii_char import *


class Ascii(tk.Tk):
    def __init__(self):
        super().__init__()
        self.creat_window()
        self.create_widgets()
        self.grid()
        # windnd.hook_dropfiles(self.text_10, func=self.drag_files)

    def creat_window(self):
        self.title('Ascii码转换')
        self.window_width = 800
        self.window_height = 200
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.window_width) // 2
        y = (screen_height - self.window_height) // 2
        self.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")

    def create_widgets(self):
        # 控件命名规则, label_00 表示在row 0，col 0 的标签
        self.label_00 = tk.Label(self, text='Ascii码16进制:')
        self.text_01 = scrolledtext.ScrolledText(self, width=50, height=1)

        self.label_10 = ttk.Label(self, text='字符:')
        self.text_11 = scrolledtext.ScrolledText(self, width=50, height=1)

        self.button_02 = ttk.Button(self, text='ascii转字符', command=self.ascii2char)
        self.button_12 = ttk.Button(self, text='字符转ascii码', command=self.char2ascii)

    def grid(self):
        self.label_00.grid(row=0, column=0, sticky=tk.W)
        self.text_01.grid(row=0, column=1, sticky=tk.W)
        self.button_02.grid(row=0, column=2, sticky=tk.W)

        self.label_10.grid(row=1, column=0)
        self.text_11.grid(row=1, column=1)
        self.button_12.grid(row=1, column=2)


    def ascii2char(self):
        ascii_hex = self.text_01.get('1.0', tk.END).rstrip()
        self.text_11.delete('1.0', tk.END)
        self.text_11.insert(tk.END, ascii_hex2char(ascii_hex))

    def char2ascii(self):
        src = self.text_11.get('1.0', tk.END).rstrip()
        self.text_01.delete('1.0', tk.END)
        self.text_01.insert(tk.END, char2ascii_hex(src))
