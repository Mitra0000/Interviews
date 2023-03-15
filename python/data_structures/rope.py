class Rope:

  def __init__(self, value: str):
    """
      Initialises a rope like so:
          O
        /
      value
    """
    self._head = Internal(Leaf(value))
    self.length = len(value)

  def get(self, idx: int) -> str:
    return self._head.find_nth(idx)

  def append(self, text: str):
    ptr = self._head
    while ptr.right and type(ptr.right) is Internal:
      ptr = ptr.right
    if not ptr.right:
      ptr.right = Leaf(text)
    else:
      ptr.right = Internal(ptr.right, Leaf(text))
    self.length += len(text)

  def extend(self, rope):
    self._head = Internal(self._head, rope._head)
    self.length += len(rope)

  def toString(self):
    self._buffer = []
    self._head.traverse(self._buffer)
    return "".join(self._buffer)

  def __len__(self):
    return self.length


class RopeNode:

  def __init__(self, offset: int):
    self.offset = offset

  def find_nth(self, n: int):
    assert False, "Method not implemented"

  def get_offset_for_parent(self):
    assert False, "Method not implemented"


class Leaf(RopeNode):

  def __init__(self, val: str):
    super().__init__(len(val))
    self.val = val

  def find_nth(self, n):
    if n >= self.offset:
      raise IndexError("Index out of range")
    return self.val[n]

  def get_offset_for_parent(self):
    return self.offset

  def traverse(self, buffer):
    buffer.append(self.val)


class Internal(RopeNode):

  def __init__(self, left=None, right=None):
    self.left = left
    self.right = right
    super().__init__(self.left.get_offset_for_parent())

  def get_offset_for_parent(self):
    return self.offset + (self.right.get_offset_for_parent()
                          if self.right else 0)

  def find_nth(self, n):
    if n < self.offset:
      return self.left.find_nth(n)
    else:
      return self.right.find_nth(n - self.offset)

  def traverse(self, buffer):
    if self.left:
      self.left.traverse(buffer)
    if self.right:
      self.right.traverse(buffer)


if __name__ == '__main__':
  rope = Rope("hello ")
  rope.append("world")
  rope.append(", how")

  new_rope = Rope(" are y")
  new_rope.append("ou")
  rope.extend(new_rope)

  print(rope.toString())
  for i in range(len(rope)):
    print(rope.get(i))
