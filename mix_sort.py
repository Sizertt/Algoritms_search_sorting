import random

def mix_sort(array):
    left = 1
    right = len(array)
    while left<right:
        for i in range(left, right):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
            if array[right-i] < array[right-i-1]:
                array[right-i], array[right-i-1] = array[right-i-1], array[right-i]
        left += 1; right -= 1
    return array
 
arr = [random.randint(0, 10) for _ in range(100)]
print(mix_sort(arr))
