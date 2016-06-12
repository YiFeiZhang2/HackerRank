#Given an undirected graph, find the shortest path from a starting node to each of the other nodes
#Used BFS with 2D array

from collections import deque

def shortestDistance(self, start):
    distance = [-1]*len(self)
    queue = deque()
    queue.append(start)
    while len(queue) != 0:
        node = queue.popleft()
        for point in self[node]:
            if distance[point] == -1 and point != start:
                queue.append(point)
                distance[point] = distance[node] +7 if distance[node] == -1 else distance[node] +6
    
    print(' '.join([str(distance[x]) for x in range(1, len(distance)) if x != start]))
            

for _ in range(int(input())):
    num_nodes, num_edges = map(int, input().strip().split(" "))
    nodes = [[] for node in range(num_nodes+1)]
    for i in range(num_edges):
        A, B = map(int, input().strip().split(" "))
        nodes[A].append(B)
        nodes[B].append(A)
    start = int(input())
    shortestDistance(nodes, start)
        
