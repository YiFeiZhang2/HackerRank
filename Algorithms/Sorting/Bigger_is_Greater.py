#given a word w, rearrange the letters of w to create a new word such that it is lexicographically greater. In case of multiple possible answers, find the lexicographically smallest among them.

for _ in range(int(input().strip())):
    arr = [x for x in input()]
    i = len(arr)-1
    while arr[i] <= arr[i-1] and i > 0:
        i -= 1
    if i == 0 or len(arr) == 1:
        print("no answer")
    else:
        j = i-1
        
        switch_val = arr[i]
        switch_ind = i
        while i < len(arr):
            if arr[i] > arr[j] and arr[i] <= switch_val:
                switch_val = arr[i]
                switch_ind = i
            i += 1
        
        piv = arr[j]
        arr[switch_ind] = piv
        arr[j] = switch_val
        
        k = j+1
        j = len(arr)-1
        while k < j:
            temp = arr[j]
            temp2 = arr[k]
            arr[j] = temp2
            arr[k] = temp
            k += 1
            j -= 1
            
        print(''.join(arr))
                
