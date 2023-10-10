# 以上题程序为例计算时间
import time
a = int(input("Input a:"))
start = time.time()
if a == 1:
    print("NO")
else:
    i = 2
    while i * i <= a:
        if a % i == 0:
            print("NO")
            break
        i = i + 1
    if i * i > a:
        print("YES")
end = time.time()
t = end - start
print("Time:" + str(t))
