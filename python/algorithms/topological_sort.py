def topological_sort(graph):
  def traverse(node):
    for neighbour in graph[node]:
        if neighbour not in unvisited:
            continue
        unvisited.remove(neighbour)
        traverse(neighbour)
    order.append(node)

  unvisited = set(graph.keys())
  order = []
  while unvisited:
      traverse(unvisited.pop())
  return order[::-1]

if __name__ == "__main__":
  graph = {
    "A": {"B", "C"},
    "B": {"E", "F"},
    "C": set(),
    "D": {"C"},
    "E": {"C"},
    "F": set(),
  }
  print(topological_sort(graph))
