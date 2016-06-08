#find if there is a common substring between two strings
#used sets, as any common substring will have at least one common letter

for _ in range(int(input())):
    A = set([x for x in input()])
    B = set([x for x in input()])
    if len(A & B) > 0:
        print("YES")
    else:
        print("NO")
