x=input("x=")
y=input("y=")
z=input("z=")
x=int(x)
y=int(y)
z=int(z)
if x>y:
    max=x
    min=y
if max<z:
    max=z
if min>z:
    min=z
print(min)
print(x+y+z-max-min)
print(max)
