import tkinter as tk

def show_selected_option():
    selected_value = radio_var.get()
    print(f"Selected option: {selected_value}")

root = tk.Tk()
root.title("Radio Button 示例")

# 创建一个变量来跟踪选择
radio_var = tk.IntVar()
radio_var.set(1)  # 设置默认选择的按钮

# 创建两个单选按钮
radio_button_1 = tk.Radiobutton(root, text="选项 1", variable=radio_var, value=1)
radio_button_2 = tk.Radiobutton(root, text="选项 2", variable=radio_var, value=2)

# 布局单选按钮
radio_button_1.pack(padx=10, pady=5)
radio_button_2.pack(padx=10, pady=5)

# 创建按钮来显示选择的选项
show_button = tk.Button(root, text="显示选择", command=show_selected_option)
show_button.pack(pady=10)

root.mainloop()
