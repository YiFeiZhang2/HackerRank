#!/usr/local/bin/python3

import re
for _ in range(int(input())):
    line = input()
    match = (bool(re.search(r'^[+-]?\d*.\d+$', line)))
    print(match)
