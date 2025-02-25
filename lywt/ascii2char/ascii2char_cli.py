import re

def char2ascii_hex(src: str, hex_head:bool=False) -> str:
    if hex_head:
        ret = ''.join([f'0X{ord(c):02x} ' for c in src])
    else:
        ret = ''.join([f'{ord(c):02x} ' for c in src])
    return ret

def modify_hex_string(src:str):
    """
    将16进制格式的字符串标准化

    example:
    >>> modify_hex_string('30 31   32  ')
    '303132'
    >>> modify_hex_string(' 0x30 0X31   0x32   ')
    '303132'
    """
    src = re.sub(r'\s+', '', src)
    src = re.sub(r'0x|0X', '', src)

    return src

def ascii_hex2char(src: str) -> str:
    try:
        return bytes.fromhex(modify_hex_string(src)).decode('utf-8')
    except Exception as e:
        print(e)
        raise ValueError('输入不合法')
