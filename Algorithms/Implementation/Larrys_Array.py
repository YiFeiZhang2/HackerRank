#!/usr/local/bin/python3

numCase = int(input())
for i in range(numCase):
    length = int(input())
    numbers = list(map(int, input().split(" ")))
    counter = 0
    for j in range(length-1):
        for k in range(j, length):
            if numbers[j] >  numbers[k]:
                #print(numbers[j])
                #print(numbers[k])
                counter += 1
    if counter%2 == 0:
        print ("YES")
    else:
        print ("NO")
