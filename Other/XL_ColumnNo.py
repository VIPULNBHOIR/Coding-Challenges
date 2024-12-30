

str1=str(input("Enter the Column of XL: "))
sum=0

for i in range (0,len(str1)):
    Num=int(-(64-ord(str1[i]))) 
    power=(len(str1)-1)-i
    sum += Num * (26**power)

print("Column Number: ",sum)