
import math

ar1=input().split()
ar2=input().split()

ar1=sorted(ar1 + ar2)

mid = math.ceil(len(ar1)/2)

if len(ar1) % 2 == 0:
   print(float((ar1[mid-1] + ar1[mid])/2)) 
else:
    print(float(ar1[mid-1]))



