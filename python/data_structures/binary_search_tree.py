from collections import deque


class BSTNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, item):
        if item <= self.val:
            if self.left:
                self.left.insert(item)
            else:
                self.left = BSTNode(item)
        else:
            if self.right:
                self.right.insert(item)
            else:
                self.right = BSTNode(item)

    def search(self, item):
        if item == self.val:
            return self
        elif item < self.val:
            if self.left:
                return self.left.search(item)
            return None
        else:
            if self.right:
                return self.right.search(item)
            return None

    def __str__(self):
        return str(self.val)

    @classmethod
    def get_as_array(cls, root):
        """ Returns the tree represented by root as an array in BFS order. """
        queue = deque([root])
        output = []
        while queue:
            node = queue.popleft()
            output.append(str(node))
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return output


if __name__ == "__main__":
    root = BSTNode(6)
    for num in [3, 7, 2, 4, 8, 9]:
        root.insert(num)
    print(BSTNode.get_as_array(root))
    print(root.search(8).right)
    """
    Tree looks like:
            6
        3       7
      2   4       8
                   9
    """
