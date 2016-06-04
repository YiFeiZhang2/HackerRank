from html.parser import HTMLParser
import re

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print (tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])

            
parser = MyHTMLParser()
for _ in range(int(input())):
    line = input().strip()
    parser.feed(line)
