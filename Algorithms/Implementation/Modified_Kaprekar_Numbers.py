#print number on a line, seperated by space if it is between
#a given upper and lower bound (inclusive)
#and if the left half + right half of the number squared is equal to the number
#if the right piece has d digits, left piece must have d or d-1 digits

lower = input()
upper = input()
counter = 0
for i in range(int(lower), int(upper)+1):
    if i == 1:
        counter +=1
        print(i, end = " ")
    else:
        temp = i**2
        right = str(temp)[int(len(str(temp))/2):]
        left = str(temp)[:int(len(str(temp))/2)]
        if left and right:
            if int(left) + int(right) == i:
                counter += 1
                print(i, end = " ")

            
if counter == 0:
    print("INVALID RANGE")
