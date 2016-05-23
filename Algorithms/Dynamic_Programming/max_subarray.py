#!/usr/local/bin/python3

numCase = int(input())
for _ in range(numCase):
    arr_length = int(input())
    arr = list(map(int, input().strip().split(" ")))
    #print(arr)
    if max(arr) < 0:
        max_contig = max(arr)
        max_non_contig = max(arr)
        print(str(max_contig) + " " + str(max_non_contig))
    else:
        max_contig = 0
        max_contig_here = 0
        max_non_contig = 0
        for number in arr:
            #print(number)
            if number > 0:
                max_non_contig += number
            if max_contig_here + number > 0:
                max_contig_here = max_contig_here + number
                max_contig = max(max_contig_here, max_contig)
                #print(max_contig)
            else:
                max_contig_here = 0
        print(str(max_contig) + " " + str(max_non_contig))
