#two players playing with n stones. each turn a player must remove 2, 3, 5 stones. first player unable to make a move loses
#print the winner based on the starting number of stones

for _ in range(int(input().strip())):
    num_stones = int(input())
    if num_stones%7 == 0 || num_stomes%7 == 1:
        print("Second")
    else:
        print("First")
