#Use bit manipulation to find the integer that occurs once, where every other integer occurs twice
#Used Bitwise XOR (^) -> x^x = 0, a^x^a = x, x^0 = 0

# Head ends here
def lonelyinteger(b):
    answer = 0
    for x in b:
        answer = answer^x
    return answer
# Tail starts here
if __name__ == '__main__':
    a = int(input())
    b = map(int, input().strip().split(" "))
    print(lonelyinteger(b))

