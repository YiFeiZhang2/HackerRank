#in place quicksort using Lomuto Partitioning method

def quicksort(self, low, high):
    if low < high:
        piv = partition(self, low, high)
        quicksort(self, low, piv-1)
        quicksort(self, piv+1, high)

def partition(self, low, high):
    piv = self[high]
    small_ind = low
    for ind in range(low, high+1):
        if self[ind] > piv:
            continue
        else:
            temp = self[ind]
            self[ind] = self[small_ind]
            self[small_ind] = temp
            small_ind += 1
    print(' '.join(str(x) for x in self))
    return small_ind-1
            
size = int(input().strip())
arr = [int(x) for x in input().strip().split(" ")]

quicksort(arr, 0, len(arr)-1)
