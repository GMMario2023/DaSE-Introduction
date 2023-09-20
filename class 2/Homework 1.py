def integerbreak(n):
    dp = [0] * (n+1) # 定义n+1维数组dp，并初始化为全零状态
    for i in range(2,n+1): #开始遍历
        for j in range(1,i):
            dp[i] = max(dp[i],max(j*(i-j),j*dp[i-j])) #前一个max函数确定是否需要划分，后一个max函数确定划分后i-j是否需要划分
    return dp[n]
k=input("输入一个正整数:")
k=int(k)
print("分解后的最大乘积为:"+str(integerbreak(k)))
