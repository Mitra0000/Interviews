# Simplified BSTNode from python/data_structures/binary_search_tree.py
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