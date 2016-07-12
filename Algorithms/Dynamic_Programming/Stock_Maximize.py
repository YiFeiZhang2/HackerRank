for _ in range(int(input().strip())):
    length = int(input().strip())
    price = list(map(int, input().strip().split(" ")))
    
    max_so_far = price[length-1]
    profit = 0
    
    for day in range(length,0,-1):
        if price[day-1] > max_so_far:
            max_so_far = price[day-1]
        else:
            profit += max_so_far - price[day-1]
            
    print(profit)
            
