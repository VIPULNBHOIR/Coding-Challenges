num=1001
counter=0

while counter <=100 :

    for i in range (2,(num//2)+1):
        if (num % i == 0):
            flag=0
            break
        else:
            flag=1

    if flag == 1:
        print(num)
        counter+=1

    num+=1    

         