L1 = input().split(' ')
N = L1[0]
Q = int(L1[1])
A0 = [int(x) for x in input().split(' ')]
A0.reverse()
B = []

primes = []
currp = 2
while len(primes) < Q:
    is_prime = True
    for p in primes:
        if currp%p == 0:
            is_prime = False
    if is_prime:
        primes.append(currp)
    currp += 1
    
for p in primes:
    A1 = []
    while len(A0) > 0:
        a = A0.pop()
        if a%p == 0:
            B.append(a)
        else:
            A1.append(a)
    A0 = A1

for x in B:
    print(x)
for x in A0:
    print(x)