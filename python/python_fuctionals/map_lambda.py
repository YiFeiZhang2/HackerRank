#!/usr/local/bin/python3

def fib(n):
    arr = [0, 1]
    for i in range(2,n+1):
        arr.append(arr[i-1] + arr[i-2])
    #print(arr)
    return arr[n]

#print(' '.join([str(fib(x)) for x in range(5)]))

#print (list(map(lambda x: fib(int(x))**3, [i for i in range(int(input()))])))
#print (list(map(lambda x: x**3, [fib(i) for i in range(int(input()))])))
print (list([fib(i)**3 for i in range(int(input()))]))
