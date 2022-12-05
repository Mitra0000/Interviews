import random


def partition(array, l, r):
    """ 
        This is just one implementation of a partition function. It is not the 
        quickest by far but it is easy to understand.
        First, separate numbers <= to the pivot into the left list and the rest 
        into the right list. Add the pivot to the end of the left list and then 
        extend it by the right list. The left list now contains the partitioned 
        numbers. All that's left to do is insert them back into the array.
    """
    left = []
    right = []
    pivot = random.randint(l, r)
    for i in range(l, r + 1):
        if i == pivot:
            continue
        if array[i] <= array[pivot]:
            left.append(array[i])
        else:
            right.append(array[i])
    pos = len(left)
    left.append(array[pivot])
    left.extend(right)
    for j in range(l, r + 1):
        array[j] = left[j - l]
    return pos


def quick_sort_recursive(array, l, r):
    if l < r:
        p = partition(array, l, r)
        quick_sort_recursive(array, l, p - 1)
        quick_sort_recursive(array, p + 1, r)


def quick_sort(array):
    quick_sort_recursive(array, 0, len(array) - 1)
    return array


if __name__ == "__main__":
    nums = list(range(20))
    random.shuffle(nums)
    print(nums)
    nums = quick_sort(nums)
    print(nums)
