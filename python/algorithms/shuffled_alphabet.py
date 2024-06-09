from collections import defaultdict
from topsort import topsort

def shuffled_alphabet(words):
  graph = defaultdict(set)
  vertices = set()
  for first, second in zip(words, words[1:]):
    for i in range(len(first)):
      if first[i] != second[i]:
        graph[first[i]].add(second[i])
        vertices.add(first[i])
        vertices.add(second[i])
        break
  return topsort(vertices, graph)

if __name__ == "__main__":
  words = ["fft", "fcp", "aac", "act", "acd", "atp", "tbk", "tdf"]
  print(shuffled_alphabet(words))
