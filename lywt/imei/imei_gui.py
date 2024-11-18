import tkinter as tk
from tkinter import ttk, StringVar
from datetime import datetime
import time
from .imei_cli import generate_imei


class IMEI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('IMEI生成')
        self.creat_vars()
        self.create_widgets()

    def creat_vars(self):
        self.barcode = StringVar()
        self.imei1 = StringVar()
        self.imei2 = StringVar()
        self.meid1 = StringVar()
        self.meid2 = StringVar()

    def create_widgets(self):
        ttk.Label(self, text='barcode').grid(row=1, column=0, padx=(10, 0), pady=(5, 0))
        barcode_entry = ttk.Entry(self, textvariable=self.barcode)
        barcode_entry.grid(row=1, column=1, padx=(10, 0), pady=(5, 0))
        barcode_entry.bind("<Button-1>", lambda event:self.copy_while_click(event, barcode_entry))

        ttk.Label(self, text='imei1').grid(row=2, column=0, padx=(10, 0), pady=(5, 0))
        imei1_enrtry = ttk.Entry(self, textvariable=self.imei1)
        imei1_enrtry.grid(row=2, column=1, padx=(10, 0), pady=(5, 0))
        imei1_enrtry.bind("<Button-1>", lambda event:self.copy_while_click(event, imei1_enrtry))

        ttk.Label(self, text='imei2').grid(row=3, column=0, padx=(10, 0), pady=(5, 0))
        imei2_entry = ttk.Entry(self, textvariable=self.imei2)
        imei2_entry.grid(row=3, column=1, padx=(10, 0), pady=(5, 0))
        imei2_entry.bind("<Button-1>", lambda event:self.copy_while_click(event, imei2_entry))

        ttk.Label(self, text='meid1').grid(row=4, column=0, padx=(10, 0), pady=(5, 0))
        meid1_entry = ttk.Entry(self, textvariable=self.meid1)
        meid1_entry.grid(row=4, column=1, padx=(10, 0), pady=(5, 0))
        meid1_entry.bind("<Button-1>", lambda event:self.copy_while_click(event, meid1_entry))

        ttk.Label(self, text='meid2').grid(row=5, column=0, padx=(10, 0), pady=(5, 0))
        meid2_entry = ttk.Entry(self, textvariable=self.meid2)
        meid2_entry.grid(row=5, column=1, padx=(10, 0), pady=(5, 0))
        meid2_entry.bind("<Button-1>", lambda event:self.copy_while_click(event, meid2_entry))

        ttk.Button(self, text='生成', command=self.gen).grid(row=6, column=1, padx=(10, 0), pady=(10, 0))

    def copy_while_click(self, event, entry: ttk.Entry):
        content = entry.get()
        if content:
            self.clipboard_clear()          # 清空剪贴板
            self.clipboard_append(content)  # 将内容复制到剪贴板
            self.update()                   # 更新剪贴板状态

    def gen(self):
        current_time = datetime.now().strftime(r'%Y%m%d%H%M%S')     # len=14
        self.barcode.set(current_time[:12])
        self.imei1.set(generate_imei(current_time))
        self.meid1.set(current_time)
        time.sleep(1)
        current_time = datetime.now().strftime(r'%Y%m%d%H%M%S')
        self.imei2.set(generate_imei(current_time))
        self.meid2.set(current_time)
        pass
