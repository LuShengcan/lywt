"""
    可视化文件 md5 获取
"""
import hashlib
import tkinter as tk
import windnd


def drag_files(files):
    for file in files:
        file = file.decode('gbk')
        text_1.insert(tk.END, file+'\n')
        with open(file, 'rb') as fr:
            text_2.insert(tk.END, hashlib.md5(fr.read()).hexdigest()+'\n')


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("900x300")

    # 组件
    label1 = tk.Label(root, text='请拖拽文件')
    text_1 = tk.Text(root, width=50, height=20, font=("黑体", 10, ""))
    text_2 = tk.Text(root, width=35, height=10, font=("黑体", 18, ""))

    # 布局
    label1.place(x=0, y=10)
    text_1.place(x=100, y=0)
    text_2.place(x=460, y=0)

    windnd.hook_dropfiles(root, func=drag_files)
    print('hello world')

    root.mainloop()
