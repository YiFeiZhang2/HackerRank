import re

for _ in range(int(input())):
    name, email = input().strip().split(" ")
    #print (email)
    if bool(re.match(r'^<[a-zA-Z][\.\w-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}>$',email)):
        print(name + " " + email)
