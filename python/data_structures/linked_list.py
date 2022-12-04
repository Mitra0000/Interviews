class LinkedListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class LinkedList:

    def __init__(self):
        self._head = None

    def get(self, idx):
        if not self._head or idx < 0:
            raise IndexError()
        pointer = self._head
        while idx > 0:
            if not pointer.next:
                raise IndexError()
            pointer = pointer.next
            idx -= 1
        return pointer

    def append(self, value):
        if not self._head:
            self._head = LinkedListNode(value)
            return
        pointer = self._head
        # Iterate to the end of the list.
        while pointer.next:
            pointer = pointer.next
        pointer.next = LinkedListNode(value)

    def insert(self, value, position):
        if position == 0:
            self._head = LinkedListNode(value, self._head)
            return
        try:
            node = self.get(position - 1)
        except IndexError:
            raise IndexError(f"Position: {position} is out of range.")
        node.next = LinkedListNode(value, node.next)

    def __str__(self):
        output = []
        pointer = self._head
        while pointer:
            output.append(str(pointer.val))
            pointer = pointer.next
        return f"[{','.join(output)}]"


if __name__ == "__main__":
    linked_list = LinkedList()
    for num in range(5):
        linked_list.append(num)
    linked_list.insert(2.5, 3)
    print(linked_list.get(4))
    print(linked_list)
