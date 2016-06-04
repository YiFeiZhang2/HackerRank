import re

for _ in range(int(input())):
    line = input().strip()
    if all([re.search(r,line)for r in [r'[a-zA-Z0-9]{10}',r'([A-Z].*){2}',r'([0-9]{1}.*){3}']]) and not re.search(r'(.).*\1', line):
        print("Valid")
    else:
        print("Invalid")

