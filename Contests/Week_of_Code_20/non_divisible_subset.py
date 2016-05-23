#!/usr/local/bin/python3

arrLength, k = map(int, input().strip().split(" "))
arr = [int(i)%k for i in input().strip().split(" ")]
sumpair = list()
counter = 0
for i in range(1,k):
    sumpair.append(arr.count(i))
for j in range(len(sumpair)//2):
    counter += max(sumpair[j], sumpair[len(sumpair)-1-j]) 
if len(sumpair)%2 == 1:
    counter += max(sumpair[j+1])
print(counter)
