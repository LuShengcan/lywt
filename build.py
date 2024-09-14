import subprocess
import os
import re
from datetime import datetime


def get_small_version(update):
    max_small_version = -1

    for file in os.listdir('dist'):
        match = re.match('.*?v(\\d+)\\.(\\d+).*?', file)
        if match:
            max_small_version = max(max_small_version, int(match.group(2)))
    if update:
        return max_small_version + 1
    else:
        return max_small_version


if __name__ == '__main__':
    APP_NAME = 'lywt'
    BIG_VERSION = '1'
    SMALL_VERSION = str(get_small_version(update=0))
    BUILD_TIME = datetime.now().strftime(r'%Y%m%d%H%M')
    VERSION = APP_NAME + '_v' + BIG_VERSION + '.' + SMALL_VERSION + '.' + BUILD_TIME

    pyinstaller_command = f'pyinstaller -n {VERSION} --noconsole main.py'
    subprocess.run(pyinstaller_command, shell=True)
