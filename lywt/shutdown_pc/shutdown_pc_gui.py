import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from .shutdown_pc_cli import shut_down_at, shutdown_after

class ShutdownPC(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.creat_window()
        self.creat_vars()
        self.create_widgets()
        self.grid_widgets()

    def creat_window(self):
        self.title('定时关机')
        self.window_width = 400
        self.window_height = 200
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.window_width) // 2
        y = (screen_height - self.window_height) // 2
        self.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")

    def creat_vars(self):
        self.hour = StringVar(value='00')
        self.minute = StringVar(value='00')
        self.radio_var = tk.IntVar(value=1)

    def create_widgets(self):
        self.combobox_hour = ttk.Combobox(self, values=[f"{i:02d}" for i in range(24)], textvariable=self.hour)
        self.combobox_minute = ttk.Combobox(self, values=[f"{i:02d}" for i in range(60)], textvariable=self.minute)

        self.radio_1 = ttk.Radiobutton(self, text="指定关机时间", variable=self.radio_var, value=1)
        self.radio_2 = ttk.Radiobutton(self, text="多长时间后关机", variable=self.radio_var, value=2)

        self.button_shutdown = ttk.Button(self, text='创建计划', command=self.make)

    def grid_widgets(self):
        self.combobox_hour.grid(row=0, column=0)
        self.combobox_minute.grid(row=0, column=1)

        self.radio_1.grid(row=1, column=0)
        self.radio_2.grid(row=1, column=1)

        self.button_shutdown.grid(row=2, column=0)

    def make(self):
        if self.radio_var.get() == 1:
            shut_down_at(int(self.hour.get()), int(self.minute.get()))
        elif self.radio_var.get() == 2:
            shutdown_after(int(self.hour.get()), int(self.minute.get()))
        else:
            pass
