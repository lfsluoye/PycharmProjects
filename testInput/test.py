__author__ = "lfs"
list = []
k = input("please input number k ")
k = int(k)
for i in range(k):
    num = input("please input num  ")
    list.append(int(num))
maxSum = 0
for i in range(k):
    tempSum = 0
    index = i
    while index<k:
        tempSum += list[index]
        if tempSum>maxSum:
            maxSum = tempSum
        index += 1


print(maxSum)
