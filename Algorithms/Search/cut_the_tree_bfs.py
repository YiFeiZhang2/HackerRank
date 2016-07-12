#With every node having a value, what edge should be cut to create two trees that have values with the smallest difference?
#BFS way - not very fast

from collections import deque
from copy import deepcopy

def calcDiff(self, A, B, vert):
    vert_list = deepcopy(vert)
    vert_list[A].remove(B)
    vert_list[B].remove(A)
    queueA = deque([A])
    queueB = deque([B])
    seen_vert = [A, B]
    val = vert_val[A] - vert_val[B]
    while len(queueA) != 0:
        curr_vert = queueA.popleft()
        for C in vert_list[curr_vert]:
            if C not in seen_vert:
                queueA.append(C)
                seen_vert.append(C)
                val += vert_val[C]
    while len(queueB) != 0:
        curr_vert = queueB.popleft()
        for D in vert_list[curr_vert]:
            if D not in seen_vert:
                queueB.append(D)
                seen_vert.append(D)
                val -= vert_val[D]
    return val

def treeDiff(self, vert_list):
    val = list()
    seen_vert = [0]
    queue = deque([0])
    curr_vert = 0
    while len(queue) != 0:
        curr_vert = queue.popleft()
        for B in vert_list[curr_vert]:
            if B not in seen_vert:
                queue.append(B)
                seen_vert.append(B)
                val.append(calcDiff(self, curr_vert, B, vert_list))
    
    val = [abs(x) for x in val]
    return min(val)

num_vert = int(input())
vert_val = list(map(int, input().strip().split(" ")))
vert = [[] for x in range(num_vert)]
for _ in range(num_vert-1):
    A, B = map(int, input().strip().split(" "))
    vert[A-1].append(B-1)
    vert[B-1].append(A-1)
print(treeDiff(vert_val, vert))
