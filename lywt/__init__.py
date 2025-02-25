import tkinter as tk
from tkinter import ttk
from .fileMD5.fileMD5_gui import FileMD5
from .ascii2char.ascii2char_gui import Ascii
from .imei.imei_gui import IMEI
from .shutdown_pc.shutdown_pc_gui import ShutdownPC
from .ncm2mp3.ncm_gui import NCM

from .imei import imei_cli
from .fileMD5.fileMD5_cli import md5
from .ascii2char.ascii2char_cli import ascii_hex2char, char2ascii_hex
from .shutdown_pc.shutdown_pc_cli import shutdown_at, shutdo


# pyqt6
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QApplication, QFileDialog, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QDragEnterEvent, QDropEvent, QFont

from .ui.Ui_MainWindow import Ui_MainWindow


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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()     # 创建 UI 实例
        self.ui.setupUi(self)         # 绑定 UI 到当前窗口

        self.init_imei_gen()
        self.init_file_md5()
        self.init_ascii2char()
        self.init_shutdown_pc()

    def init_imei_gen(self):
        """初始化号段生成页"""

        # 点击文本控件后把值复制到剪贴板
        fields = ["barcode", "imei_1", "imei_2", "meid_1", "meid_2", "batsn_1", "batsn_2"]
        for field in fields:
            ui_element: QLineEdit = getattr(self.ui, field)
            ui_element.mousePressEvent = lambda event, w=ui_element: self.copy_to_clipboard(w)

        self.ui.generateButton.clicked.connect(self.generate_numbers)  # 生成号段按钮点击事件

    def copy_to_clipboard(self, widget: QLineEdit):
        """复制文本到剪贴板"""
        clipboard = QApplication.clipboard()
        clipboard.setText(widget.text())

    def generate_numbers(self):
        device_info = imei_cli.generate_device_info()

        fields = ["barcode", "imei_1", "imei_2", "meid_1", "meid_2", "batsn_1", "batsn_2"]

        for field in fields:
            ui_element: QLineEdit = getattr(self.ui, field)
            ui_element.setText(getattr(device_info, field))

    def init_file_md5(self):
        self.ui.btn_selectFile.clicked.connect(lambda: self.add_files(self.select_file()))

        self.ui.md5Table.setColumnCount(2)
        self.ui.md5Table.setHorizontalHeaderLabels(["文件路径", "MD5 值"])
        self.ui.md5Table.setColumnWidth(0, 440)  # 设置第一列宽度
        self.ui.md5Table.setColumnWidth(1, 255)  # 设置第二列宽度
        self.ui.md5Table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)  # 只读模式

        self.setAcceptDrops(True)   # 设置窗口支持拖放

    def add_files(self, files):
        # add file and md5 to list
        for file in files:
            rc = self.ui.md5Table.rowCount()
            self.ui.md5Table.insertRow(rc)

            path_item = QTableWidgetItem(file)
            path_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)   # 允许复制
            self.ui.md5Table.setItem(rc, 0, path_item)

            md5_item = QTableWidgetItem(md5(file))
            md5_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            self.ui.md5Table.setItem(rc, 1, md5_item)

    def select_file(self):
        file_paths, _ = QFileDialog.getOpenFileNames(self, "选择文件")
        return file_paths

    def dragEnterEvent(self, event: QDragEnterEvent):
        """处理拖动进入事件"""
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        """处理文件拖放事件"""
        if event.mimeData().hasUrls():
            files = []
            for url in event.mimeData().urls():
                files.append(url.toLocalFile())

            self.add_files(files)

    def init_ascii2char(self):
        font = QFont("Consolas", 14)
        self.ui.hexEdit.setFont(font)
        self.ui.strEdit.setFont(font)

        self.ui.hex2strButton.clicked.connect(self.hex2str)
        self.ui.str2hexButton.clicked.connect(self.str2hex)

    def hex2str(self):
        src = self.ui.hexEdit.toPlainText()
        ret = ascii_hex2char(src)
        self.ui.strEdit.setPlainText(ret)

    def str2hex(self):
        src = self.ui.strEdit.toPlainText()

        if self.ui.if0xCheckBox.isChecked():
            ret = char2ascii_hex(src, True)
        else:
            ret = char2ascii_hex(src)

        self.ui.hexEdit.setPlainText(ret)

    def init_shutdown_pc(self):
        self.ui.hourSpinBox.setRange(0,23)
        self.ui.hourSpinBox.setWrapping(True)

        self.ui.minuteSpinBox.setRange(0, 59)
        self.ui.minuteSpinBox.setWrapping(True)

        self.ui.createPlanPushButton.clicked.connect(self.shutdown_pc)

    def shutdown_pc(self):
        selected_radio_id = self.ui.shutdownButtonGroup.checkedId()
        if selected_radio_id == self.ui.shutdownButtonGroup.id(self.ui.atRadioButton):


        elif selected_radio_id == self.ui.shutdownButtonGroup.id(self.ui.afterRadioButton):


