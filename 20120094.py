from collections import defaultdict

class Graph:
    def __init__(self, start):
        self.vertices = defaultdict(set)
        self.start = start

    def add_edge(self, v1, v2):
        if v1 == v2 or v1 in self.vertices[v2]:
            return

        self.vertices[v1].add(v2)
        self.vertices[v2].add(v1)

    def dfs(self):
        print(self.start, end=' ')
        stack = [self.start]
        checked = {self.start}

        while stack:
            neighbors = list(self.vertices[stack[-1]] - checked)
            if len(neighbors) == 0:
                stack.pop()

            else:
                neighbors.sort()
                if not neighbors[0] in checked:
                    print(neighbors[0], end=' ')
                    stack.append(neighbors[0])
                    checked.add(neighbors[0])

    def bfs(self):
        print(self.start, end=' ')
        queue = [self.start]
        checked = {self.start}

        while queue:
            neighbors = self.vertices[queue[0]]
            if len(neighbors) > 1:
                neighbors = list(neighbors)
                neighbors.sort()

            for neighbor in neighbors:
                if not neighbor in checked:
                    print(neighbor, end=' ')
                    queue.append(neighbor)
                    checked.add(neighbor)

            queue.pop(0)


_, edges, start = [ int(x) for x in input().split() ]

graph = Graph(start)

for _ in range(edges):
    v1, v2 = input().split()
    graph.add_edge(int(v1), int(v2))

graph.dfs()
print('')
graph.bfs()