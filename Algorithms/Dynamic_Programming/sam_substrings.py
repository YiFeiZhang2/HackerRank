# Sam and Substrings challenge on hackerrank
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = input()

# S[i] = total sum of sub-strings from N[0] to N[i]
# A[i] = sum of substrings that include N[i]
# S[0] = A[0] = 1
# S[i] = S[i-1] + A[i] 
#      = total sum of sub-strings that don't include N[i] + total sum of sub-strings that do
# A[i] = A[i-1]*10 + N[i]*(i+1)
#      = previous sum * 10, as all numbers are shifted left, and then N[i] is appended to the end

S = [0] * len(N)
A = [0] * len(N)

for i in range(len(N)):
    if i == 0:
        S[i] = int(N[i])
        A[i] = int(N[i])
    else:
        A[i] = (A[i-1]*10 + int(N[i])*(i+1)) % 1000000007
        S[i] = (S[i-1] + A[i]) % 1000000007
        
print(S[-1])
                
                
    