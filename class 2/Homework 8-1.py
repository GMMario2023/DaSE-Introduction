#方法1 pi/2=1-1/3+(1/3)*(2/5)+(1/3)*(2/5)*(3/7)*...
j = 1
sum = 1
i = 1
while(i<=1000):
    j = j*(i/(2*i+1))
    sum=sum+j
    i=i+1
print("%.13f"%(2*sum))