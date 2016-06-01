length = int(input())
XML = ''.join(input() for _ in range(length))
counter = 0
for _ in XML:
    if _ == '=':
        counter += 1
        
print(counter)


#More legit way?

import xml.etree.ElementTree as etree

length = int(input())
XML = ''.join(input() for _ in range(length))
tree = etree.ElementTree(etree.fromstring(XML))

def find_score(node):
    return len(node.attrib) + sum(find_score(child) for child in node)
    
print(find_score(tree.getroot()))

