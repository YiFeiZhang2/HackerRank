#!/usr/local/bin/python3
import re

line = input()
output = sorted(line, key=lambda x: (x.isdigit(), bool(re.match(r"02468", x)), x.isupper(), x.islower(), x))
print(*output , sep = '')
