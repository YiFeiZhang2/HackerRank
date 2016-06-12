from collections import defaultdict
from collections import deque

class Graph:
    def __init__ (self):
        self.vertices = defaultdict(set)
    
    def addVertex(self, vertex):
        self.vertices[vertex] = set()
    
    def addEdge(self, start_vertex, end_vertex):
        self.vertices[start_vertex].add(end_vertex)
        
    def shortestPath(self, start_vertex):
        queue = deque()
        steps = [-1]*101
        steps[1] = 0
        queue.append(start_vertex)
        
        while len(queue) != 0:
            currVert = queue.popleft()
            for vert in self.vertices[currVert]:
                if steps[vert] == -1:
                    queue.append(vert)
                    steps[vert] = steps[currVert] +1
                    
        print(steps[100])

for _ in range(int(input())):
    numladders = int(input())
    ladders = dict([tuple(map(int, input().strip().split(" "))) for x in range(numladders)])
    numsnakes = int(input())
    snakes = dict([tuple(map(int, input().strip().split(" "))) for x in range(numsnakes)])
    graph = Graph()
    for i in range(1, 100):
        graph.addVertex(i)
        for j in range(i+1, i+7):
            if j <= 100:
                if j in ladders.keys():
                    graph.addEdge(i, ladders[j])
                elif j in snakes.keys():
                    graph.addEdge(i, snakes[j])
                else:
                    graph.addEdge(i, j)
                    
    graph.shortestPath(1)
