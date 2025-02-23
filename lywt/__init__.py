import tkinter as tk
from tkinter import ttk
from .fileMD5.fileMD5_gui import FileMD5
from .ascii2char.ascii2char_gui import Ascii
from .imei.imei_gui import IMEI
from .shutdown_pc.shutdown_pc_gui import ShutdownPC
from .ncm2mp3.ncm_gui import NCM

import sys

# pyqt6
from PyQt6.QtWidgets import QApplication, QMainWindow

from .Ui_MainWindow import Ui_MainWindow


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('实用工具集合')
        # self.geometry(f'650x350+{int(self.winfo_screenwidth()*0.35)}+{int(self.winfo_screenheight()*0.25)}')

        notebook = ttk.Notebook(self)
        notebook.pack(fill=tk.X, padx=5)

        self.imei = IMEI(self)
        self.filemd5 = FileMD5(self)
        self.ascii = Ascii(self)
        self.shutdownpc = ShutdownPC(self)
        self.ncm = NCM(self)

        notebook.add(self.imei, text='  号段生成  ')
        notebook.add(self.filemd5, text='  文件md5计算  ')
        notebook.add(self.ascii, text='  编码转换  ')
        notebook.add(self.shutdownpc, text='  计划关机  ')
        notebook.add(self.ncm, text='  网易云音乐ncm格式转换  ')


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 通过 setupUi 加载 UI
        self.init_ui()  # 可选：初始化一些额外的 UI 逻辑

    def init_ui(self):
        # 这里可以添加按钮、输入框等组件的事件绑定
        self.pushButton.clicked.connect(self.on_button_click)

    def on_button_click(self):
        self.label.setText("按钮被点击了！")  # 例如更改一个 QLabel 的文本
