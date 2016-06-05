import re
line = input().strip()
#print(len(re.findall(r'(.)(?!.\1)', line)))
print(bool(re.search(r'^[1-9]{1}[0-9]{5}$', line) and len(re.findall(r'(.)(?=.\1)', line)) < 2))

