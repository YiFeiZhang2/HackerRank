numStudents = int(input())
timeList = [int(x) for x in input().split(' ')]
finishList = [0 for i in range(numStudents)]
for i in range(numStudents):
    if timeList[i] == 0:
        continue
    elif timeList[i] >= numStudents:
        continue
    else:
        finishList[(i+1)%numStudents] += 1
        finishList[((i+1)-timeList[i])%numStudents] -= 1
        
largestIndex = 0
largestFinisher = -1000000
currentFinisher = 0
for i in range(2*numStudents):
    currentFinisher = currentFinisher + finishList[i%numStudents]
    if currentFinisher > largestFinisher:
        largestFinisher = currentFinisher
        largestIndex = i%numStudents

#print(finishList)
print(largestIndex+1)