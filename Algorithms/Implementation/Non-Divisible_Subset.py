
n, k = list(map(int, input().strip().split()))
S = list(map(lambda x: int(x)%k, input().strip().split()))
sp = [0]*k
for ele in S:
    sp[ele] += 1
    
total = 0
if sp[0] != 0:
    total = 1

for i in range(1, k//2 + 1):
    if i == k-i:
        total += min(sp[i], 1)
    else:
        total += max(sp[i], sp[k-i])

print(total)