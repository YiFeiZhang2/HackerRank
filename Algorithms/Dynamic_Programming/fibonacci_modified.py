first, second, N = map(int, input().strip().split(" "))
for _ in range(3, N+1):
    curr = second*second + first
    first = second
    second = curr
    
print(curr)
