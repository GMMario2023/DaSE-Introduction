#输出成绩等级
score = int(input("输入成绩:"))
if score >= 90:
    print("优秀")
elif score >= 75:
    print("良好")
elif score >= 60:
    print("合格")
else:
    print("不合格")
