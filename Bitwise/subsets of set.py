

A=[1,2,3,4]

for i in range(1 << len(A)):
    print("{", end='')
    for j in range(len(A)):
        if (i & (1 << j)):

            print(f"{A[j]},", end='')
        
    print("}, ", end='')
    
