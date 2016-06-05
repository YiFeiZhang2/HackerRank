import re

for _ in range(int(input())):
    line = input().strip()
    if all([re.search(pattrn, line) for pattrn in [r'^[456]{1}.{15,18}$', r'^([0-9]{4}-?){3}[0-9]{4}$']]) and not re.search(r'.*(\d)(?=(\1-?){3,})', line):
        print("Valid")
    else:
        print("Invalid")
        
         
