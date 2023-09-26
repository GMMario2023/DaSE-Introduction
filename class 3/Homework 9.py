import random
#数组构建
n = int(input("Input n:"))
A = [0] * n
B = [1] * n
#下面对数组A随机赋值
for i in range(0,n):
    A[i] = int(random.uniform(1,10))
print("A = " + str(A))
#下面对数组B赋值
for i in range(0,n):
    for j in range(0,n):
        if j != i:
            B[i] = B[i] * A[j]
print("B = "+ str(B))
