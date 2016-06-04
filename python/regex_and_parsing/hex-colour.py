import re

for _ in range(int(input())):
    line = input()
    match = re.findall(r'#[a-fA-F0-9]{3,6}(?=[;,\.\)])', line)
    #print(match)
    if match:
        print ('\n'.join(match))
