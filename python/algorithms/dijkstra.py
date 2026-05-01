from helper.hash_heap import HashHeap
from helper.tube_map import tube_map

class DijkstraSolver:
    """
        A class for finding the shortest path in a graph utilising a HashHeap
        as its queue implementation.
    """
    def init(self, graph, start, end):
        self.start = start
        self.end = end
        self.__d = defaultdict(lambda: float('inf'))
        self.__d[start] = 0
        self.__p = {}
        self.__p[start] = None
        self.__visited = set()
        queue = []
        for node in graph:
            queue.append([self.__d[node], node])
        self.__queue = HashHeap(queue)

    def dijkstra(self, graph, start, end):
        self.init(graph, start, end)

        while self.__queue:
            node = self.__queue.extractMin()
            for neighbour in graph[node]:
                self.__relax(node, neighbour, graph[node][neighbour])
            self.__visited.add(node)

        return self.__generatePath()

    def __relax(self, u, v, w):
        if self.__d[u] + w < self.__d[v]:
            self.__d[v] = self.__d[u] + w
            if v not in self.__visited:
                self.__queue.update(v, self.__d[v])
            self.__p[v] = u

    def __generatePath(self):
        path = []
        node = self.end
        while node != self.start:
            path.append(node)
            node = self.__p[node]
        result = str(self.__d[self.end]) + ": "
        result += self.start
        while path:
            result += " -> " + path.pop()
        return result

if __name__ == "__main__":
    graph = tube_map
    start = "Leicester Square"
    end = "Blackfriars"
    solver = DijkstraSolver()
    print(solver.dijkstra(graph, start, end))
