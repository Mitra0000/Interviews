from helper.simple_bst import BSTNode


def pre_order_traversal(node):
    yield node.val
    if node.left:
        yield from pre_order_traversal(node.left)
    if node.right:
        yield from pre_order_traversal(node.right)


def in_order_traversal(node):
    if node.left:
        yield from in_order_traversal(node.left)
    yield node.val
    if node.right:
        yield from in_order_traversal(node.right)


def post_order_traversal(node):
    if node.left:
        yield from post_order_traversal(node.left)
    if node.right:
        yield from post_order_traversal(node.right)
    yield node.val


if __name__ == "__main__":
    root = BSTNode(6)
    for num in [3, 7, 2, 4, 8, 9]:
        root.insert(num)
    print(list(pre_order_traversal(root)))
    print(list(in_order_traversal(root)))
    print(list(post_order_traversal(root)))
