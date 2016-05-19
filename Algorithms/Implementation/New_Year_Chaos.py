#!/usr/loca/bin/python3

numCase = int(input())
for i in range(numCase):
    length = int(input())
    final = list(map(int, input().split(" ")))
    numSwitches = [0]*(length+1)
    counter = 0
    isSorted = False
    isChaotic = False
    while not isSorted:
        #print(numSwitches)
        isSorted = True
        for j in range(len(final)-1):
            final_curr = final[j]
            final_next = final[j+1]
            if final_curr > final_next:
                isSorted = False
                #print(numSwitches[final_curr])
                if numSwitches[final_curr] == 2:
                    #print(numSwitches[final_curr])
                    isSorted = True
                    isChaotic = True
                    break
                else:
                    counter += 1
                    final[j] = final_next
                    final[j+1] = final_curr
                    numSwitches[final_curr] += 1
    if isChaotic:
        print ("Too chaotic")
    else:
        print (counter)
