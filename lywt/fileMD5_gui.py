"""
    可视化文件 md5 获取
"""
import hashlib
import tkinter as tk
import windnd

class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.make_window()

    def make_window(self) -> None:
        self.geometry("900x600")
        self.title('文件MD5获取')
        label1 = tk.Label(self, text='请拖拽文件')
        text_1 = tk.Text(self, width=50, height=20, font=("黑体", 10, ""))
        text_2 = tk.Text(self, width=35, height=10, font=("黑体", 18, ""))

        label1.grid(row=0, column=0)
        text_1.grid(row=0, column=1)
        text_2.grid(row=0, column=2)

        windnd.hook_dropfiles(self, func=self.drag_files())

    def drag_files(self, files, entry: tk.Entry) -> None:
        for file in files:
            file = file.decode('gbk')
            entry.insert(tk.END, file+'\n')
            with open(file, 'rb') as fr:
                entry.insert(tk.END, hashlib.md5(fr.read()).hexdigest()+'\n')


if __name__ == '__main__':
    app = App()
    app.mainloop()
