import random
import math
def square_root(times):
    sum =0
    for i in range(times):
        x=random.uniform(2,3)
        y=random.uniform(0,14)
        d=y-(x**2)-4*x*(math.sin(x))
        if d <0:
            sum+=1
    print((14*sum)/(times))
square_root(1000000)
