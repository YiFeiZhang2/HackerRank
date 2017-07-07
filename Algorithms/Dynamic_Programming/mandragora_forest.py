# Mandragora Forest challenge on HackerRank
t = int(input().strip())
for i in range(t):
    t = int(input().strip())
    s = 1
    arr = sorted([int(x) for x in input().strip().split(' ')])
    cul_vals = [0]*t
    cul_vals[t-1] = arr[t-1]
    for j in range(t-2, -1, -1):
        cul_vals[j] = arr[j] + cul_vals[j+1]
    max_points = 0
    for j in range(0, t):
        max_points = max(max_points, (s)*cul_vals[j])
        s += 1
    #print(cul_vals)
    print(max_points)
        
        