#!/usr/local/bin/python3

import calendar

s = list(map(int, input().split(" ")))
month = s[0]
day = s[1]
year = s[2]


print(calendar.day_name[calendar.weekday(year, month, day)].upper())
