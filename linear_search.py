import random

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [random.randint(0, 100) for i in range(100)]
target = 5
print("индекс", target, "в", arr, ":", linear_search(arr, target))
