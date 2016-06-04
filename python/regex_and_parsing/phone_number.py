import re
numCase = int(input())
for _ in range(numCase):
    number = input()
    if bool(re.search(r'^(7|8|9)\d{9}$',number)):
        print("YES")
    else:
        print("NO")
