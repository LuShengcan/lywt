import hashlib


def md5(path):
    try:
        with open(path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except:
        return 'fail to open file'


if __name__ == '__main__':
    while True:
        path = input('please input file path:')
        print(md5(path))
