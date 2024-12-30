size= int(input())
arr=[ [0]*size for _ in range(size)]
num=1

for i in range (size//2 + 1):

    for j in range (i,size-i):
        arr[i][j]=num
        num+=1
    
    for j in range (i+1,size-i):
        arr[j][size-i-1]=num
        num+=1
    
    for j in range (size-i-2,i-1,-1):
        arr[size-i-1][j]=num
        num+=1
    
    for j in range (size-i-2,i,-1):
        arr[j][i]=num
        num+=1

for i in range (len(arr)):
    for j in range (len(arr)):
        print(arr[i][j], end="\t")
        
    print()

"""

range               arr_ele
--------------------------------------------------------------------

i,size-i            arr[i][j] keep row constant change column by 1

i+1,size-i          arr[j][size-1-i] keep column constant change row by 1

size-i-2,i-1,-1     arr[size-1-i][j] keep row constant change column by 1

size-i-2,i,-1       arr[j][i] keep column constant change row by 1

"""


