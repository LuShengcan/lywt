from typing import IO
import os

"""
这是一个文件处理的包，目前有的功能:
    splitByLines: 将大文件按每个文件 linesPerFile 行分割成若干个小文件

    
"""


def splitByLines(src: str, dst: str, linesPerFile=100000, encoding='utf-8'):
    '''
    scr: 源文件
    dst: 存储目录
    linesPerfile: 每个小文件的行数
    encoding: 编码
    '''

    # 确定要解析的文件
    if not os.path.exists(src):
        print(f"path '{src}' not exists!")
        return

    # 确定存储目录
    if os.path.exists(dst):
        if not os.path.isdir(dst):
            print(f'dst:{dst} is not a dst!')
            return
    else:
        os.mkdir(dst)

    # 开始处理
    numOfLine = 0   # 总行数
    numOfFile = 0   # 生成的文件个数
    fw: IO = None
    with open(src, 'r', encoding=encoding) as fr:
        for line in fr:
            if numOfLine % linesPerFile == 0:
                if fw:
                    fw.close()
                fileName = os.path.basename(src)
                prefix = os.path.splitext(fileName)[0]
                suffix = os.path.splitext(fileName)[1]
                filePath = os.path.join(dst, f'{prefix}_{numOfFile}{suffix}')
                fw = open(filePath, 'w', encoding=encoding)
                numOfFile += 1

                fw.write(line)
            else:
                fw.write(line)
            numOfLine += 1
        if fw:
            fw.close()
    print(f"总行数{numOfLine}，每个文件{linesPerFile}行，总共生成了{numOfFile}个文件")

def splitBySize(src: str, dst:str, sizePerFile=1):
    pass
