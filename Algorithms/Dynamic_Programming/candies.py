# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
rank_arr = []
candy_arr = [1] * N
for i in range(N):
    rank_arr.append(int(input()))
    
for i in range(1, N):
    if rank_arr[i] > rank_arr[i-1]:
        candy_arr[i] = candy_arr[i-1] + 1
        
#print(candy_arr)
        
for i in range(N-2, -1, -1):
    if rank_arr[i] > rank_arr[i+1] and candy_arr[i] <= candy_arr[i+1]:
        candy_arr[i] = candy_arr[i+1] + 1
        
#print(candy_arr)
        
print(sum(candy_arr))