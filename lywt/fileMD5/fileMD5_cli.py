import hashlib


def md5(path: str) -> str:
    md5 = hashlib.md5()

    try:
        with open(path, 'rb') as f:
            while chunk := f.read(8192):
                md5.update(chunk)
    except Exception as e:
        return e

    return md5.hexdigest()


if __name__ == '__main__':
    while True:
        path = input('please input file path:')
        print(md5(path))
