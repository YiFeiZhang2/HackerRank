#!/bin/python3
import sys


numCases = int(input().strip())
for a0 in range(numCases):
    R,C = input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    #G_i = 0
    for G_i in range(R):
        G_t = str(input().strip())
        G.append(G_t)
    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    isContain = False
    
    #P_i = 0
    for P_i in range(r):
        P_t = str(input().strip())
        P.append(P_t)
    
    counter = 0
    isTrue = False
    for i in range(0, R - r + 1):
        for j in range(0, C - c + 1):
            if P[0][0] == G[i][j]:
                counter = 0
                for k in range(r):
                        if P[k] in G[i+k] and P[k][0] == G[i+k][j]:
                            counter += 1
                        else:
                            break
                            break
                
                if counter == r:
                    print("YES")
                    isTrue = True
                    break
                    break
                
    if not isTrue:
        print("NO")
