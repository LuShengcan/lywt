import tkinter as tk
from tkinter import ttk, StringVar
from datetime import datetime
import time
from .cli import generate_imei


class IMEI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.creat_window()
        self.creat_vars()
        self.create_widgets()
        self.grid_widgets()

    def creat_window(self):
        self.title('IMEI生成')
        self.window_width = 400
        self.window_height = 250
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.window_width) // 2
        y = (screen_height - self.window_height) // 2
        self.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")

    def creat_vars(self):
        self.barcode = StringVar()
        self.imei1 = StringVar()
        self.imei2 = StringVar()
        self.meid1 = StringVar()
        self.meid2 = StringVar()

    def create_widgets(self):

        self.label_barcode = ttk.Label(self, text='barcode')
        self.entry_barcode = ttk.Entry(self, textvariable=self.barcode)

        self.label_imei1 = ttk.Label(self, text='imei1')
        self.entry_imei1 = ttk.Entry(self, textvariable=self.imei1)

        self.label_imei2 = ttk.Label(self, text='imei2')
        self.entry_imei2 = ttk.Entry(self, textvariable=self.imei2)

        self.label_meid1 = ttk.Label(self, text='meid1')
        self.entry_meid1 = ttk.Entry(self, textvariable=self.meid1)

        self.label_meid2 = ttk.Label(self, text='meid2')
        self.entry_meid2 = ttk.Entry(self, textvariable=self.meid2)

        self.button_gen = ttk.Button(self, text='生成', command=self.gen)

    def grid_widgets(self):

        self.label_barcode.grid(row=1, column=0, padx=(10, 0), pady=(5, 0))
        self.entry_barcode.grid(row=1, column=1, padx=(10, 0), pady=(5, 0))

        self.label_imei1.grid(row=2, column=0, padx=(10, 0), pady=(5, 0))
        self.entry_imei1.grid(row=2, column=1, padx=(10, 0), pady=(5, 0))

        self.label_imei2.grid(row=3, column=0, padx=(10, 0), pady=(5, 0))
        self.entry_imei2.grid(row=3, column=1, padx=(10, 0), pady=(5, 0))

        self.label_meid1.grid(row=4, column=0, padx=(10, 0), pady=(5, 0))
        self.entry_meid1.grid(row=4, column=1, padx=(10, 0), pady=(5, 0))

        self.label_meid2.grid(row=5, column=0, padx=(10, 0), pady=(5, 0))
        self.entry_meid2.grid(row=5, column=1, padx=(10, 0), pady=(5, 0))

        self.button_gen.grid(row=6, column=1, padx=(10, 0), pady=(10, 0))

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
