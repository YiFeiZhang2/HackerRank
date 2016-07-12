size = int(input().strip())
numbers = list(map(int, input().strip().split()))
occur = [0 for _ in range(100)]

for num in numbers:
    occur[num] += 1

for x in range(100):
    for _ in range(occur[x]):
        print(x, end = ' ')
    
