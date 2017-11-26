__author__ = "lfs"
import random
import time
import copy
import sys
def cal_time(func):
    def wrapper(*args, **kwargs):
        ti = time.time()
        x = func(*args, **kwargs)
        ti2 = time.time()
        print("Time cost:", func.__name__, ti2 - ti)
        return x
    return wrapper

@cal_time
def bubble_sort(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]

@cal_time
def bubble_sort_1(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            break
@cal_time
def select_spot(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]

@cal_time
def insert_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] > tmp:
            li[j+1]=li[j]
            j = j - 1
        li[j+1] = tmp

def quick_sort_x(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        quick_sort_x(data, left, mid - 1)
        quick_sort_x(data, mid + 1, right)
def partition(data, left, right):
    tmp = data[left]
    while left < right:
        while left < right and data[right] >= tmp:
            right -= 1
        data[left] = data[right]
        while left < right and data[left] <= tmp:
            left += 1
        data[right] = data[left]
    data[left] = tmp
    return left
@cal_time
def quick_sort(data):
    return  quick_sort_x(data, 0, len(data) - 1)
@cal_time
def sys_sort(data):
    return data.sort()

def merge_sort_x(data):
    n = len(data)
    if n <= 1:
        return data
    mid = n//2
    left_li = merge_sort_x(data[:mid])
    right_li = merge_sort_x(data[mid:])
    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result
@cal_time
def merge_sort(data):
    merge_sort_x(data)

# def sift(data, low, high):
#     i = low
#     j = 2*i + 1
#     tmp = data[i]
#     while j <= high:
#         if j < high and data[j] < data[j + 1]:
#             j += 1
#         if tmp < data[j]:
#             data[i] = data[j]
#             i = j
#             j = 2*i + 1
#         else:
#             break
#     data[i] = tmp
# def hep_sort(data):






sys.setrecursionlimit(100000)
data = list(range(5000))
random.shuffle(data)
data1 = copy.deepcopy(data)
data2 = copy.deepcopy(data)
data3 = copy.deepcopy(data)
data4 = copy.deepcopy(data)
# bubble_sort(data1)
bubble_sort_1(data1)
# select_spot(data)
# insert_sort(data)
quick_sort(data2)
sys_sort(data3)
data5 = merge_sort_x(data4)
print(data)
print(data1)
print(data2)
print(data3)
print(data4)
print(data5)