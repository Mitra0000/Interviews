class TrieNode:
  """ A single Trie Node. """
  def __init__(self, char):
      # Character stored in this node.
      self.char = char

      # Whether this can be the end of a word.
      self.is_end = False

      # Dictionary of child nodes. {Chars: Nodes}.
      self.children = {}


class Trie(object):
  def __init__(self):
      # The Trie starts with a root node which doesn’t 
      # store a character.
      self.root = TrieNode("")

  def insert(self, word):
    node = self.root

    for char in word:
      if char in node.children:
        node = node.children[char]
      else:
        new_node = TrieNode(char)
        node.children[char] = new_node
        node = new_node

    node.is_end = True

  def query(self, prefix):
    self.output = []
    node = self.root

    for char in prefix:
      if char in node.children:
        node = node.children[char]
      else:
        return []
    # Remove last character as it will be appended as the current node char.
    self.dfs(node, prefix[:-1])

    return sorted(self.output)

  def dfs(self, node, prefix):
    if node.is_end:
      self.output.append(prefix + node.char)
    for child in node.children.values():
      self.dfs(child, prefix + node.char)

if __name__ == "__main__":
  trie = Trie()
  trie.insert("hello")
  trie.insert("world")
  trie.insert("head")
  trie.insert("help")
  trie.insert("won")
  print(trie.query("he"))
  print(trie.query("w"))
