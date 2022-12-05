class MaxHeap:

    def __init__(self, iterable=[]):
        self._heap = iterable
        self._build_max_heap()

    def peek(self):
        """ Returns the biggest item in the heap in O(1) time. """
        assert len(self._heap) > 0, "Cannot peek with empty heap."
        return self._heap[0]

    def pop(self):
        """ Returns & removes the biggest item in the heap in O(logn) time. """
        assert len(self._heap) > 0, "Cannot pop from an empty heap."
        self._swap_at_indices(0, len(self._heap) - 1)
        item = self._heap.pop()
        self._max_heapify(0)
        return item

    def insert(self, item):
        """ Inserts item in the correct place in the heap in O(logn) time. """
        idx = len(self._heap)
        self._heap.append(item)
        while item > self._heap[(idx - 1) // 2] and idx != 0:
            self._swap_at_indices(idx, (idx - 1) // 2)
            idx = (idx - 1) // 2

    def _max_heapify(self, idx):
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left >= len(self._heap):
            # No children, return.
            return
        elif right >= len(self._heap):
            # One child.
            if self._heap[idx] < self._heap[2 * idx + 1]:
                self._swap_at_indices(idx, 2 * idx + 1)
                self._max_heapify(2 * idx + 1)
        else:
            # Two children.
            if self._heap[idx] < self._heap[left] or self._heap[
                    idx] < self._heap[right]:
                if self._heap[left] > self._heap[right]:
                    self._swap_at_indices(idx, left)
                    self._max_heapify(left)
                else:
                    self._swap_at_indices(idx, right)
                    self._max_heapify(right)

    def _build_max_heap(self):
        for i in range(len(self._heap) // 2, -1, -1):
            self._max_heapify(i)

    def _swap_at_indices(self, idx1, idx2):
        self._heap[idx1], self._heap[idx2] = self._heap[idx2], self._heap[idx1]

    def __str__(self):
        return str(self._heap)


if __name__ == "__main__":
    heap = MaxHeap()
    for i in range(5):
        heap.insert(i)
    print(heap)

    heap = MaxHeap(list(range(5)))
    print(heap)

    print(heap.pop())
    print(heap)
