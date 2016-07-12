#2 players playing on a 15x15 board, where a coin starts at a random x, y coordinate.
#each move a player moves the coin to x-2, y+1 or x-2, y-1 or x+1, y-2 or x-1, y-2
#first player unable to make a move loses
#find out who that is
for _ in range(int(input().strip())):
    x, y = map(int, input().strip().split())
    x = x%4
    y = y%4
    if x == 0 or x == 3 or y == 0 or y == 3:
        print("First")
    else:
        print("Second")
