
# 16进制按字节转换为字符
def HexByte2Char(txt: str):
    chars = [chr(int(txt[i:i+2], 16)) for i in range(0, len(txt), 2)]
    return ''.join(chars)

if __name__ == '__main__':
    txt = '73'
    print(HexByte2Char(txt))
