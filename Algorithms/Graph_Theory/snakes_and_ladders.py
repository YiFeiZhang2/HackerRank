from collections import defaultdict

class Graph:
    def __init__ (self):
        self.vertices = defaultdict(set)
    
    def addVertex(self, vertex):
        self.vertices[vertex.value] = set()
    
    def addEdge(self, start, end):
        self.vertices[start.value].add(end.value)
        
    def shortestPath(self, start, end):
        for value in self.vertices[start]:
            print(value)
        
class Vertex:
    def __init__(self, value):
        self.value = value
        self.seen = False

for _ in range(int(input())):
    numladders = int(input())
    ladders = dict([tuple(map(int, input().strip().split(" "))) for x in range(numladders)])
    numsnakes = int(input())
    snakes = dict([tuple(map(int, input().strip().split(" "))) for x in range(numsnakes)])
    graph = Graph()
    for i in range(1, 100):
        graph.addVertex(Vertex(i))
        for j in range(i+1, i+7):
            if j <= 100:
                if j in ladders.keys():
                    graph.addEdge(Vertex(i), Vertex(ladders[j]))
                elif j in snakes.keys():
                    graph.addEdge(Vertex(i), Vertex(snakes[j]))
                else:
                    graph.addEdge(Vertex(i), Vertex(j))
                
    graph.shortestPath(1, 100)
