import tkinter as tk
from tkinter import ttk
from .fileMD5.fileMD5_gui import FileMD5
from .ascii2char.ascii2char_gui import Ascii
from .imei.imei_gui import IMEI
from .shutdown_pc.shutdown_pc_gui import ShutdownPC


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('文件处理工具')
        self.create_widgets()

    def create_widgets(self):
        ttk.Button(self, text='文件MD5计算', width=15, command=self.fileMD5).grid(row=0, column=0, sticky=tk.W, padx=2, pady=2)
        ttk.Button(self, text='ascii和字符转换', width=15, command=self.ascii).grid(row=0, column=1, sticky=tk.W, padx=2, pady=2)
        ttk.Button(self, text='号段生成', width=15, command=self.imei).grid(row=1, column=0, sticky=tk.W, padx=2, pady=2)
        ttk.Button(self, text='计划关机', width=15, command=self.ShutdownPC).grid(row=1, column=1, sticky=tk.W, padx=2, pady=2)

    def fileMD5(self):
        subWin = FileMD5(self)
        subWin.grab_set()

    def ascii(self):
        subWin = Ascii(self)
        subWin.grab_set()

    def imei(self):
        subWin = IMEI(self)
        subWin.grab_set()

    def ShutdownPC(self):
        subWin = ShutdownPC(self)
        subWin.grab_set()
