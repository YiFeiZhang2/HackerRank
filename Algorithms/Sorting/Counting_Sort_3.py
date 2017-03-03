size = int(input().strip())
occur = [0]*100

for _ in range(size):
    num = int(input().strip().split(" ")[0])
    #print(num)
    occur[num] += 1

x = 0   
for i in range(100):
    x += occur[i]
    #print(occur[i])
    print (x, end = " ")
