import xml.etree.ElementTree as etree
length = int(input())
XML = ''.join(input() for _ in range(length))

def findDepth (depth, node):
    if len(node) > 0:
        depth = max(findDepth(depth+1, child) for child in node)
    return depth

tree = etree.ElementTree(etree.fromstring(XML))

print(findDepth(0, tree.getroot()))
