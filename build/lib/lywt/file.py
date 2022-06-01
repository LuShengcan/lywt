'''
    这是一个文件处理的包，目前有的功能:
        splitBigFile: 将大文件按每个文件 linesPerFile 行分割成若干个小文件
'''

def splitBigFile(src:str, dest:str, linesPerFile=100000,encoding:str = 'utf-8'):
    suffix = src.split('.')[-1]
    with open(src, 'r', encoding=encoding) as fr:
        lineNum = 0
        fileNum = 0
        lines = []
        while 1:
            if lineNum < linesPerFile:
                line = fr.readline()
                if not line:
                    if lineNum == 0:
                        return
                    else:
                        with open(dest+'/split_file_'+str(fileNum)+'.'+suffix, 'w', encoding=encoding) as fw:
                            fw.writelines(lines)
                        return
                else:
                    lines.append(line)
                    lineNum += 1
            else:
                with open(dest+'/split_file_'+str(fileNum)+'.'+suffix, 'w', encoding=encoding) as fw:
                    fw.writelines(lines)
                lineNum = 0
                fileNum += 1
                lines = []