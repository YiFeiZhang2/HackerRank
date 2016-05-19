#!/usr/bin/local/python3

from datetime import datetime
numCase = int(input())
time_format = "%a %d %b %Y %H:%M:%S %z"

for i in range(numCase):
    time1 = datetime.strptime(input(), time_format)
    time2 = datetime.strptime(input(), time_format)
    print(abs(int((time1-time2).total_seconds())))
 
