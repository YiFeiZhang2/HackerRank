import re

numerals = input()
print (bool(re.search(r'^M{0,3}(CM|CD|D?C{0,3})(XL|XC|L?X{0,3})(IX|IV|V?I{0,3})$', numerals)))
