stackA = []
stackB = []
for i in range(int(input())):
    l = [int(x) for x in input().split()]
    if l[0] == 1:
        stackA.append(l[1])
    elif l[0] == 2:
        if not stackB:
            while stackA:
                stackB.append(stackA.pop())
        stackB.pop()
    else:
        if not stackB:
            while stackA:
                stackB.append(stackA.pop())
        print(stackB[-1])
            