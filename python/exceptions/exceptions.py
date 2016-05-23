#!/usr/local/bin/python3

for _ in range(int(input())):
    try:
        a, b = map(int, input().strip().split(" "))
        print(a//b)
    except (ZeroDivisionError, ValueError) as e:
        print('Error Code: ' + str(e))
