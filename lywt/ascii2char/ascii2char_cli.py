
def char2ascii_hex(src: str) -> str:
    return ''.join([f'{ord(c):02x} ' for c in src])


def ascii_hex2char(src: str) -> str:
    return bytes.fromhex(src).decode('utf-8')


if __name__ == '__main__':
    src = '616263'
    print(ascii_hex2char(src))
