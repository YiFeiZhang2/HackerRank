#!/usr/local/bin/python3

import sys


h = int(input().strip())
m = int(input().strip())

time_dic = dict()
time_dic[1] = "one"
time_dic[2] = "two"
time_dic[3] = "three"
time_dic[4] = "four"
time_dic[5] = "five"
time_dic[6] = "six"
time_dic[7] = "seven"
time_dic[8] = "eight"
time_dic[9] = "nine"
time_dic[10] = "ten"
time_dic[11] = "eleven"
time_dic[12] = "twelve"
time_dic[13] = "thirteen"
time_dic[14] = "fourteen"
time_dic[16] = "sixteen"
time_dic[17] = "seventeen"
time_dic[18] = "eighteen"
time_dic[19] = "nineteen"
time_dic[20] = "twenty"
time_dic[21] = "twenty one"
time_dic[22] = "twenty two"
time_dic[23] = "twenty three"
time_dic[24] = "twenty four"
time_dic[25] = "twenty five"
time_dic[26] = "twenty six"
time_dic[27] = "twenty seven"
time_dic[28] = "twenty eight"
time_dic[29] = "twenty nine"

if m == 30:
    print("half past " + time_dic[h])
elif m == 15:
    print("quarter past " + time_dic[h])
elif m == 0:
    print(time_dic[h] +" o' clock")
elif (m-30) > 0:
    if m%15 == 0:
        print("quarter to "  + time_dic[h+1])
    else:
        print( time_dic[abs(m-60)] + " minutes to " + time_dic[h+1])
else:
    print(time_dic[m] + " minutes past " + time_dic[h])
