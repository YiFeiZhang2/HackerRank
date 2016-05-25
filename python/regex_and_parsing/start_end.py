#!/usr/local/bin/python3

import re

S = input()
j = input()
match = re.finditer(r'(?='+j+'), S)
if re.search(r''+j+'', S):
	print ('\n'.join([str((x.start(), x.start()+len(j)-1)) for x in match]))
else:
	print((-1, -1))
