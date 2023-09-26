#用正则表达式验证身份证号是否合法(前17位为数字，18为数字或X)
import re
ID = str(input("Input ID number:"))
if re.match(r"(^\d{15}$)|(^\d{17}([0-9]|X)$)",ID):
    print("Legal")
else:
    print("Illegal")
