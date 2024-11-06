import tkinter as tk
from tkinter import ttk
from tkinter import StringVar, messagebox
from .shutdown_pc_cli import shut_down_at, shutdown_after, cancel_shutdown


class ShutdownPC(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.creat_window()
        self.creat_vars()
        self.create_widgets()

    def creat_window(self):
        self.title('定时关机')

    def creat_vars(self):
        self.hour = StringVar(value='00')
        self.minute = StringVar(value='00')
        self.radio_var = tk.IntVar(value=1)

    def create_widgets(self):
        self.f0 = ttk.Frame(self)
        self.f0.pack(side=tk.TOP, padx=2, pady=2)

        ttk.Label(self.f0, text="时间/时长选择:").grid(row=0, column=0, padx=2, pady=2)
        ttk.Combobox(self.f0, values=[f"{i:02d}" for i in range(24)], textvariable=self.hour).grid(row=0, column=1, padx=2, pady=2)
        ttk.Combobox(self.f0, values=[f"{i:02d}" for i in range(60)], textvariable=self.minute).grid(row=0, column=2, padx=2, pady=2)

        ttk.Label(self.f0, text="关机类型:").grid(row=1, column=0, sticky=tk.W, padx=2, pady=2)
        ttk.Radiobutton(self.f0, text="指定关机时间", variable=self.radio_var, value=1).grid(row=1, column=1, sticky=tk.W, padx=2, pady=2)
        ttk.Radiobutton(self.f0, text="多长时间后关机", variable=self.radio_var, value=2).grid(row=1, column=2, sticky=tk.W, padx=2, pady=2)

        ttk.Button(self.f0, text='创建计划', command=self.make).grid(row=2, column=1, sticky=tk.W, padx=2, pady=2)
        ttk.Button(self.f0, text='取消计划', command=self.cancel).grid(row=2, column=2, sticky=tk.W, padx=2, pady=2)

    def make(self):
        status = self.radio_var.get()
        if status == 1:
            shut_down_at(int(self.hour.get()), int(self.minute.get()))
        elif status == 2:
            shutdown_after(int(self.hour.get()), int(self.minute.get()))
        else:
            pass

    def cancel(self):
        ret = cancel_shutdown()
        if ret == 1116:
            messagebox.showerror('错误', '当前没有任何生效的关机计划')