#!/usr/local/bin/python3

import re

for _ in range(int(input())):
    #ptrn = re.compile(r"\s([&]|[|]){2}\s")
    print(re.sub(r"(?<=\s)([&]{2}|[|]{2})(?=\s)", lambda x: "and" if x.group() == '&&' else "or", input()))
