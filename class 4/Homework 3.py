# 以数组[1, 0, 2, 6, 3, 5, 4, 7]为例
def insertionSort(arr):
    for i in range(len(arr)):
        preIndex = i - 1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex + 1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex + 1] = current
    return arr

array = [1, 0, 2, 6, 3, 5, 4, 7]
print(str(array) + "->" + str(insertionSort(array)))

