from datetime import datetime, timedelta
import random
from collections import namedtuple


def generate_imei(imei_14: str):
    if len(imei_14) != 14:
        print("ERROR! Please input a 14-digit IMEI!")
        return

    if not imei_14.isnumeric():
        print("ERROR! Please input a numeric IMEI!")
        return

    sum1 = 0
    for i, var in enumerate(imei_14):
        var_int = int(var)
        if i % 2 == 1:
            doubled = var_int * 2
            sum1 += doubled // 10 + doubled % 10
        else:
            sum1 += var_int

    bit = (10 - sum1 % 10) % 10
    return f'{imei_14}{bit}'


def generate_device_info():
    # 电池序列号: 7+3+7, 中间3位是生产日期
    year = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
            'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    month = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C']

    day = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X']

    current_time = datetime.now()
    time_1 = current_time.strftime(r'%Y%m%d%H%M%S')     # len=14
    time_2 = (current_time + timedelta(seconds=1)).strftime(r'%Y%m%d%H%M%S')

    barcode = time_1[:12]
    imei_1 = generate_imei(time_1)
    imei_2 = generate_imei(time_2)
    meid_1 = time_1
    meid_2 = time_2
    batsn_1 = time_1[:7] + random.choice(year) + random.choice(month) + random.choice(day) + time_1[:7]
    batsn_2 = time_2[:7] + random.choice(year) + random.choice(month) + random.choice(day) + time_2[:7]

    device_info = namedtuple("device_info", ['barcode', 'imei_1', 'imei_2', 'meid_1', 'meid_2', 'batsn_1', 'batsn_2'])

    return device_info(barcode, imei_1, imei_2, meid_1, meid_2, batsn_1, batsn_2)
