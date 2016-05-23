import re

line = re.search(r"([a-zA-Z0-9])\1", input().strip())
print(line.group(1) if line else -1)
