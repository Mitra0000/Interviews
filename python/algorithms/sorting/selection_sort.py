import random

def selection_sort(array):
    for idx in range(len(array)):
        min_idx = -1
        min_num = float('inf')
        for j in range(idx, len(array)):
            if array[j] < min_num:
                min_num = array[j]
                min_idx = j
        array[idx], array[min_idx] = array[min_idx], array[idx]
    return array

if __name__ == "__main__":
    nums = list(range(20))
    random.shuffle(nums)
    print(nums)
    nums = selection_sort(nums)
    print(nums)
