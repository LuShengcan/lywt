from PIL import Image
import os


def compress(infile, outfile, target_kb, step=1):
    size = os.path.getsize(infile)/1024
    img = Image.open(infile)
    if size <= target_kb:
        img.save(outfile, quality=95)   # 质量 1到95,由低到高

    else:
        now_size = size
        qua = 95
        while now_size > target_kb:
            qua -= step
            if qua <= 1:
                break
            img.save(outfile, quality=qua)
            print(qua)
            now_size = os.path.getsize(outfile)/1024


if __name__ == '__main__':
    in_name = 'C:/lsc_files/blog-pictures/1.jpg'
    directory, suffix = os.path.splitext(in_name)       # 将路径和后缀分开
    out_name = '{}-out{}'.format(directory, suffix)     # 拼凑成新名字
    print(out_name)
    compress(in_name, out_name, 20)
