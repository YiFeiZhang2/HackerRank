#using sets to find the answer in linear time
#ori = set of the original numbers
#diff = original numbers + difference (k)
#numbers in both sets represent the larger value in the pairs whose difference is equal to k
#the length of that set is the answer

# Head ends here
def pairs(a,k):
    # a is the list of numbers and k is the difference value
    ori = set(a)
    diff = set([x + k for x in ori])
    both = ori & diff
    answer = len(both)
    return answer
# Tail starts here
if __name__ == '__main__':
    a = input().strip()
    a = list(map(int, a.split(' ')))
    _a_size=a[0]
    _k=a[1]
    b = input().strip()
    b = list(map(int, b.split(' ')))
    print(pairs(b,_k))

