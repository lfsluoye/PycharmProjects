__author__ = "lfs"
import time
import random


def cal_time(func):
    def wrapper(*args, **kwargs):
        ti = time.time()
        x = func(*args, **kwargs)
        ti2 = time.time()
        print("Time cost:", func.__name__, ti2 - ti)
        return x
    return wrapper

@cal_time
def bin_search(data_set, val):
    low = 0
    high = len(data_set) - 1
    while low <= high:
        mid = (low + high) // 2
        if data_set[mid] == val:
            return mid
        elif data_set[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return

datalist = list(range(100000))
bin_search(datalist, 234)
