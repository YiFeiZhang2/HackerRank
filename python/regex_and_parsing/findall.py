import re

vowels = re.findall(r"(?<=[^AEIOUaeiou])([AEIOUaeiou]{2,})(?=[^AEIOUaeiou])", input().strip())
print('\n'.join(vowels) if vowels else -1)
