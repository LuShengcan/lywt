import tkinter as tk
from tkinter import ttk
from .fileMD5.fileMD5_gui import FileMD5
from .ascii2char.ascii2char_gui import Ascii
from .imei.imei_gui import IMEI

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.create_window()
        self.create_widgets()
        self.grid_widgets()

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
        self.button_10 = ttk.Button(self, text='ascii和字符转换', command=self.ascii)
        self.button_20 = ttk.Button(self, text='号段生成', command=self.imei)


    def grid_widgets(self):
        self.button_00.grid(row=0, column=0)
        self.button_10.grid(row=1, column=0)
        self.button_20.grid(row=2, column=0)


    def fileMD5(self):
        subWin = FileMD5(self)
        subWin.grab_set()

    def ascii(self):
        subWin = Ascii(self)
        subWin.grab_set()

    def imei(self):
        subWin = IMEI(self)
        subWin.grab_set()
