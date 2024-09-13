import tkinter as tk
from tkinter import ttk

# 子窗口类
class ToolWindow(tk.Toplevel):
    def __init__(self, parent, tool_name):
        super().__init__(parent)
        self.title(f"{tool_name} 窗口")
        self.geometry("300x200")
        label = ttk.Label(self, text=f"这是 {tool_name} 的子窗口")
        label.pack(pady=20)

# 主窗口类
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("工具集合")
        self.geometry("400x300")

        label = ttk.Label(self, text="请选择工具")
        label.pack(pady=20)

        # 创建多个工具按钮
        tools = ["工具1", "工具2", "工具3"]
        for tool in tools:
            btn = ttk.Button(self, text=tool, command=lambda t=tool: self.open_tool(t))
            btn.pack(pady=10)

    def open_tool(self, tool_name):
        # 打开子窗口
        tool_window = ToolWindow(self, tool_name)
        tool_window.grab_set()  # 使得子窗口为模式窗口

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
