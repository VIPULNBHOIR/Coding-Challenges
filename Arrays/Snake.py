row,column=3,3
ele=1

arr=[ [0]*column for _ in range (row) ]

k=column
for i in range (row):
    if k>=column-1:
        start= 0
        end= column
        inc_dec= 1
    if k <= 0:
        start= column-1
        end= -1
        inc_dec= -1

    for j in range(start,end,inc_dec):
        arr[i][j]=ele
        k= start
        ele += 1

for ele in arr:
    print(ele)
