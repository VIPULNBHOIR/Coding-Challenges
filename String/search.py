string1="vipul is ggoodgood as well goods"
find=" "
count=0
j=0
At_index=[]
for i in range (len(string1)):

    if(string1[i]==find[j]):
        j+=1
    else:
        if(string1[i]==find[0]):
            j=1
        else:
            j=0
        

    if(j==len(find)):
        count+=1
        At_index.append(i - (len(find)-1))
        j=0



print(count)
print(At_index)