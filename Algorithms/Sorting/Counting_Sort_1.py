#Print the number of times each value appears, where the value is between 0 and 100

size = int(input().strip())
count = [0]*100
for x in input().strip().split(" "):
    if int(x) < 100:
        count[int(x)] += 1
print(' '.join(map(str, count)))

