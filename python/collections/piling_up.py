#!/usr/local/bin/python3

from collections import deque
for _ in range(int(input())):
    d = deque()
    length = int(input())
    d.extend(input().strip().split(" "))
    isPossible = True
    if length < 2:
        print("Yes")
    else:
        left = int(d.popleft())
        right = int(d.pop())
        top = 2**31
        #print(top)
        while len(d) != 0:
            if right >= left and right <= top:
                top = max(left, right)
                right = int(d.pop())
                
                #print(top)
            elif left > right and left <= top:
                top = max(left, right)
                left = int(d.popleft())
                
                #print(top)
            else:
                isPossible = False
                break    
        if right > top or left > top:
            isPossible = False
        if isPossible:
            print("Yes")
        else:
            print("No")
