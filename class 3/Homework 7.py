#用更相减损术求最大公约数
a = int(input("Input a:"))
b = int(input("Input b:"))
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print("(a,b) = " + str(a))
