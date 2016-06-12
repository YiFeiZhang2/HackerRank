#given graph with nodes and varying edge length, find the shortest distance from start node to all other nodes, -1 of not possible
#used bfs with arrays of tuples, which were in the format (node value, distance)


from collections import deque

def shortestPath(self, start_node):
    shortest_distance = [0]*(len(self)+1)
    queue = deque()
    queue.append(start_node)
    
    while len(queue) != 0:
        curr_node = queue.popleft()
        for node_tuple in self[curr_node[0]]:
            node_value = node_tuple[0]
            distance = node_tuple[1] + shortest_distance[curr_node[0]]
            if shortest_distance[node_value] == 0 or shortest_distance[node_value] > distance:
                shortest_distance[node_value] = distance
                queue.append(node_tuple)
                
    print(' '.join([str(shortest_distance[x]) if shortest_distance[x] != 0 else '-1' for x in range(1, len(self)) if x != start_node[0]]))
    

for _ in range(int(input())):
    num_nodes, num_edges = map(int, input().strip().split(" "))
    nodes = [[] for x in range(num_nodes +1)]
    for edge in range(num_edges):
        A, B, length = map(int, input().strip().split(" "))
        nodes[A].append((B, length))
        nodes[B].append((A, length))
    start_node = int(input())
    
    shortestPath(nodes, (start_node, 0))

