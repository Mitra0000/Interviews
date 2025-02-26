import random

def bubble_sort(array):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                sorted = False
                array[i], array[i+1] = array[i+1], array[i]
    return array

if __name__ == "__main__":
    nums = list(range(20))
    random.shuffle(nums)
    print(nums)
    nums = bubble_sort(nums)
    print(nums)
