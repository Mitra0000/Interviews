import heapq
import random

def heap_sort(iterable):
    sorted_list = []
    heapq.heapify(iterable)
    while iterable:
        sorted_list.append(heapq.heappop(iterable))
    return sorted_list

if __name__ == "__main__":
    numbers = [18, 9, 15, 4, 0, 13, 11, 8, 3, 10, 1, 14, 6, 7, 5, 16, 2, 17, 12]
    print(heap_sort(numbers))