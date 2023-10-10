a = int(input("Input a:"))
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
