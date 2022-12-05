import heapq
import random


def heap_sort(iterable):
    heapq.heapify(iterable)
    return [heapq.heappop(iterable) for i in range(len(iterable))]


if __name__ == "__main__":
    numbers = [18, 9, 15, 4, 0, 13, 11, 8, 3, 10, 1, 14, 6, 7, 5, 16, 2, 17, 12]
    print(heap_sort(numbers))
