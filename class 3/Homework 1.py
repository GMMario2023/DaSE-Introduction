#十进制小数与二进制小数转化，其中整数部分使用bin函数，小数部分使用自定义函数point_dec_to_bin
def point_dec_to_bin(point_dec):
    binstr = "" #binstr存放小数部分转化后二进制的字符串，保留15位
    for i in range(1,16):
        point_dec *= 2
        if point_dec >= 1:
            point_dec -= 1
            binstr += "1"
        else:
            binstr += "0"
    return binstr
#主程序
dec_n = float(input("Input a number:"))
int_dec_n = int(dec_n)
point_dec_n = dec_n - int_dec_n
int_bin_n = bin(int_dec_n)
print(str(dec_n) + " = " + int_bin_n + "." + point_dec_to_bin(point_dec_n))
