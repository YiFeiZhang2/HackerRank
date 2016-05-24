#!/use/local/bin/python3

import re

numEmails = int(input())
emails = [input() for i in range(numEmails)]

ptrn = re.compile('^[\w-]+@[a-zA-Z0-9]+\\.[\w]{1,3}$')
print(sorted(list(filter(lambda x: ptrn.search(x), emails))))
