

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

