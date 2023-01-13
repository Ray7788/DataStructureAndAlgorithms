i = 0
A = [0,0,0,0,0,0,0,0,0,0,0] 
while(i < len(A) and A[i] == 1):
    A[i] = 0
    i = i + 1

if i < len(A):
    A[i] = 1

print(A)