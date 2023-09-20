# 开立方 牛顿法
def Cube_root_3():
    c = 10
    g = c/2
    i = 0
    while (abs(g**3-c)>0.00000000001):
        g = (2*g + c/(g**2))/3
        i = i+1
        print ("%d:%.13f"%(i,g))

Cube_root_3()
