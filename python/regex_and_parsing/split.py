#!/usr/local/bin/python3

import re

print('\n'.join(re.split("[,.]*", input().strip("[.,]"))))
