import heapq

class HashHeap:
    """ An efficient priority queue implementation for Dijkstra's. """
    def __init__(self, items):
        self.__items = items
        heapq.heapify(self.__items)
        self.__lookup = {}
        for i, (_, node) in enumerate(self.__items):
            self.__lookup[node] = i

    def update(self, node, val):
        idx = self.__lookup[node]
        self.__items[idx][0] = val
        if idx // 2 < 0 or self.__items[idx][0] > self.__items[idx // 2][0]:
            self.heapify(idx)
            return
        while idx // 2 >= 0 and self.__items[idx][0] < self.__items[idx // 2][0]:
            self.swap(idx, idx // 2)
            idx = idx // 2

    def extractMin(self):
        if len(self.__items) == 0:
            return None
        self.swap(0, len(self.__items) - 1)
        smallest = self.__items.pop()
        del self.__lookup[smallest[1]]
        if len(self.__items) > 0:
            self.heapify(0)
        return smallest[1]

    def swap(self, idx1, idx2):
        self.__items[idx1], self.__items[idx2] = self.__items[idx2], self.__items[idx1]
        self.__lookup[self.__items[idx1][1]] = idx1
        self.__lookup[self.__items[idx2][1]] = idx2

    def heapify(self, idx):
        current = self.__items[idx][0]
        leftIdx = idx * 2 + 1
        rightIdx = idx * 2 + 2
        left = self.__items[leftIdx][0] if leftIdx < len(
            self.__items) else float('inf')
        right = self.__items[rightIdx][0] if rightIdx < len(
            self.__items) else float('inf')
        if current > left or current > right:
            if left < right:
                self.swap(idx, leftIdx)
                self.heapify(leftIdx)
            else:
                self.swap(idx, rightIdx)
                self.heapify(rightIdx)

    def __bool__(self):
        return len(self.__items) > 0
