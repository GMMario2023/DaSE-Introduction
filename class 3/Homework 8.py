#生成2个数组，其中一个长度为3，另一个长度为5，对第一个数组进行冒泡排序，对第二个数组进行选择排序
import random
list_1 = [0,0,0]
list_2 = [0,0,0,0,0]
#对两个数组进行随机赋值，结果在1-50之间
for i in range(0,3):
    list_1[i] = int (random.uniform(1,50))
for i in range(0,5):
    list_2[i] = int (random.uniform(1,50))
print("First list is: " + str(list_1))
print("Second list is: " + str(list_2))
#对第一个数组进行冒泡排序，使其递增
for i in range(2,0,-1):
    for j in range(0,i):
        if list_1[j+1] < list_1[j]:
            t = list_1[j]
            list_1[j] = list_1[j+1]
            list_1[j+1] = t
print("Sorted first list is: " + str(list_1))
#对第二个数组进行选择排序，使其递减
for i in range(0,5):
    max = list_2[i]
    for j in range(i+1,5):
        if list_2[j] > max:
            imax = j
    t = list_2[i]
    list_2[i] = list_2[imax]
    list_2[imax] = t
print("Sorted second list is: " + str(list_2))
