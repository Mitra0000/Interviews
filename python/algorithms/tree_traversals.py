from helper.simple_bst import BSTNode


class PreOrderTraverser:

    @classmethod
    def traverse(cls, node):
        cls._order = []
        cls._traverse_internal(node)
        return cls._order

    @classmethod
    def _traverse_internal(cls, node):
        cls._order.append(node.val)
        if node.left:
            cls._traverse_internal(node.left)
        if node.right:
            cls._traverse_internal(node.right)


class InOrderTraverser:

    @classmethod
    def traverse(cls, node):
        cls._order = []
        cls._traverse_internal(node)
        return cls._order

    @classmethod
    def _traverse_internal(cls, node):
        if node.left:
            cls._traverse_internal(node.left)
        cls._order.append(node.val)
        if node.right:
            cls._traverse_internal(node.right)


class PostOrderTraverser:

    @classmethod
    def traverse(cls, node):
        cls._order = []
        cls._traverse_internal(node)
        return cls._order

    @classmethod
    def _traverse_internal(cls, node):
        if node.left:
            cls._traverse_internal(node.left)
        if node.right:
            cls._traverse_internal(node.right)
        cls._order.append(node.val)


if __name__ == "__main__":
    root = BSTNode(6)
    for num in [3, 7, 2, 4, 8, 9]:
        root.insert(num)
    print(list(PreOrderTraverser.traverse(root)))
    print(list(InOrderTraverser.traverse(root)))
    print(list(PostOrderTraverser.traverse(root)))
