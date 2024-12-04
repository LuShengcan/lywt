from ctypes import windll, c_char_p


def decrypt_file(file_path: str) -> str:
    # 加载 DLL
    pDll = windll.LoadLibrary('./MyDecrypt.dll')
    pDll.MyDecryptFile.restype = c_char_p

    # 将字符串转换为 C 字符串并传递给函数, 因为系统是gbk编码，所以调整为gbk
    ret = pDll.MyDecryptFile(file_path.encode('gbk'))

    print(ret,file=open('1.xml','w'))

    print(ret[42540:42560])

    wrong = ret[42540:42560].decode('gbk')
    print(wrong)

decrypt_file('Z2339-BDT-00_BDT.script')
