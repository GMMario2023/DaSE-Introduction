# 开平方3 牛顿法
def Square_root_3():
    c = 2000
    g = c/2
    i = 0
    while (abs(g*g-c)>0.00000000001):
        g = (g + c/g)/2
        i = i+1
        print ("%d:%.13f"%(i,g))

Square_root_3()
