#use default dict to count occurence
#use set to find unique numbers that appear are different rates in A and B
#print them out

from collections import defaultdict

sizeA = int(input())
A = list(map(int, input().strip().split(" ")))
sizeB = int(input())
B = list(map(int, input().strip().split(" ")))
numDict = defaultdict(int)
for num in A:
    numDict[num] += 1
for num in B:
    numDict[num] -= 1
diff = set()
for number in iter(numDict):
    if numDict[number] != 0:
        diff.add(number)

print(' '.join([str(x) for x in sorted(diff)]))


