pos_num=[]
def big(list1):

    list1[0]=str(list1[0])
    list1[1]=str(list1[1])
    list1[2]=str(list1[2])

    for i in range(len(list1)):

        if(i==0):
            pos_num.append(list1[i]+list1[i+1]+list1[i+2])
            pos_num.append(list1[i]+list1[i+2]+list1[i+1])

        elif(i==1):
            pos_num.append(list1[i]+list1[i+1]+list1[i-1])
            pos_num.append(list1[i]+list1[i-1]+list1[i+1])

        else:
            pos_num.append(list1[i]+list1[i-1]+list1[i-2])
            pos_num.append(list1[i]+list1[i-2]+list1[i-1])

    return  max((pos_num))

lis=[58,50,800]
print(big(lis))

# T.C= O(n) 
# S.C= O(2*n)

