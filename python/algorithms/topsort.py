def topsort(vertices, edges):
  unvisited = vertices
  order = []
  while unvisited:
    node = unvisited.pop()
    traverse(node, edges, unvisited, order)
  return order[::-1]

def traverse(node, edges, unvisited, order):
  for neighbour in edges[node]:
    if neighbour in unvisited:
      unvisited.remove(i)
      traverse(neighbour, edges, unvisited, order)
  order.append(node)

if __name__ == "__main__":
  vertices = {"A", "B", "C", "D", "E", "F"}
  edges = {
    "A": ["B", "C"],
    "B": [],
    "C": ["D"],
    "D": ["E", "F"],
    "E": ["F"],
    "F": ["B"],
  }
  print(topsort(vertices, edges))
