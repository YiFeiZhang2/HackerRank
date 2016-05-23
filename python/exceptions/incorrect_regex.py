#!/usr/local/bin/python3

import re
for _ in range(int(input())):
	try:
		regex = re.compile(input().strip())
		print(True)
	except Exception as e:
		print(False)
