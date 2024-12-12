import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import time
import threading
import os
from .ncm_cli import dump


def select_directory(var: tk.StringVar):
    directory = filedialog.askdirectory()
    if directory:
        var.set(directory)


def select_file(var: tk.StringVar):
    file = filedialog.askopenfilename()
    if file:
        var.set(file)


class NCM(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # 变量
        self.src_dir = tk.StringVar()
        self.dst_dir = tk.StringVar()
        self.src_files = None
        self.log = tk.StringVar()
        self.running = False

        # 控件
        f0 = ttk.Frame(self)
        f0.pack(fill=tk.X)

        ttk.Entry(f0, textvariable=self.src_dir, width=40).grid(row=0, column=0, padx=2, pady=2)
        ttk.Button(f0, command=lambda: select_directory(self.src_dir), text='源文件目录').grid(row=0, column=1, padx=2, pady=2)

        ttk.Entry(f0, textvariable=self.dst_dir, width=40).grid(row=1, column=0, padx=2, pady=2)
        ttk.Button(f0, command=lambda: select_directory(self.dst_dir), text='输出目录').grid(row=1, column=1, padx=2, pady=2)

        self.start_button = ttk.Button(f0, text='开始批量转换', command=self.start_conversion)
        self.start_button.grid(row=2, column=0, padx=2, pady=2)

        self.stop_button = ttk.Button(f0, text='停止批量转换', command=self.stop_conversion)
        self.stop_button.grid(row=2, column=1, padx=2, pady=2)

        ttk.Label(f0, textvariable=self.log).grid(row=3, column=0, padx=2, pady=2)

    def start_conversion(self):
        if not self.running:
            self.running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            threading.Thread(target=self.convert).start()

    def stop_conversion(self):
        if self.running:
            self.running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.log.set('转换已停止')

    def convert(self):
        src_dir = self.src_dir.get()
        dst_dir = self.dst_dir.get()

        if not os.path.isdir(dst_dir):
            messagebox.showerror('错误', f'{dst_dir} 不是一个目录')
            return

        for file_name in os.listdir(src_dir):
            if not self.running:
                break
            file_path = os.path.join(src_dir, file_name)
            if os.path.isfile(file_path):
                if os.path.splitext(file_path)[1] == ".ncm":
                    try:
                        dump(file_path, dst_dir)
                        self.log.set(f'finish {file_name}')
                    except Exception as e:
                        print(e)
                        print(f'something went wrong when process {file_name}')

            time.sleep(1)
            self.update()  # 更新界面

        if self.running:
            self.log.set('全部转换完成')
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
