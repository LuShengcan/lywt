import subprocess
import os
import re


def get_small_version():
    max_small_version = -1

    for file in os.listdir('dist'):
        match = re.match('.*?_v(\\d+)\\.(\\d+)', file)
        if match:
            max_small_version = max(max_small_version, int(match.group(2)))

    return max_small_version + 1


if __name__ == '__main__':
    APP_NAME = 'lywt'
    BIG_VERSION = '1'
    SMALL_VERSION = str(get_small_version())
    VERSION = APP_NAME + BIG_VERSION + '.' + SMALL_VERSION

    # 设置 PyInstaller 命令
    pyinstaller_command = f'pyinstaller -n {VERSION} --noconsole main.py'

    # 执行 PyInstaller 命令
    subprocess.run(pyinstaller_command, shell=True)
