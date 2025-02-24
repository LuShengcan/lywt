import os
import subprocess

ui_dir = './lywt/ui'

for root, _, files in os.walk(ui_dir):
    for file in files:
        if file.endswith(".ui"):
            ui_file = os.path.join(root, file)  # 获取完整的 .ui 文件路径
            py_file = os.path.join(root, f"UI_{file.replace('.ui', '.py')}")  # 目标 .py 文件路径

            # 构建 pyuic6 命令
            cmd = ["pyuic6", "-o", py_file, ui_file]
            print(f"转换 {ui_file} → {py_file}")

            # 执行命令
            subprocess.run(cmd, check=True)

print("所有 UI 文件转换完成！")
