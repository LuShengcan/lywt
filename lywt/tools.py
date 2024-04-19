import tkinter as tk
from tkinter import ttk
from .gui.fileMD5_gui import FileMD5
from .gui.ascii_char_gui import Ascii


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.create_window()
        self.create_widgets()
        self.grid()

    def create_window(self):
        self.title('文件处理工具')
        self.window_width = 600
        self.window_height = 400
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.window_width) // 2
        y = (screen_height - self.window_height) // 2
        self.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")

    def create_widgets(self):
        self.button_00 = ttk.Button(self, text='文件MD5计算', command=self.fileMD5)
        self.button_01 = ttk.Button(self, text='ascii和字符转换', command=self.ascii)

    def grid(self):
        self.button_00.grid(row=0, column=0)
        self.button_01.grid(row=0, column=1)

    def fileMD5(self):
        subWin = FileMD5()
        subWin.attributes('-topmost', True)
        subWin.mainloop()

    def ascii(self):
        subWin = Ascii()
        subWin.attributes('-topmost', True)
        subWin.mainloop()