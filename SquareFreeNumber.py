def isSFN(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            dev =  i 
            if (dev ** 0.5) % 1 == 0:
                return False

            cotient = num // i
            if (cotient ** 0.5) % 1 == 0:
                return False
    
    return True
    
    
num = int(input())
factors = []
count = 0

for i in range(1, int(num ** 0.5) + 1):
    if num % i == 0:
        if i != 1:
            factors.append(i)
        factors.append(num // i)

print(factors)

for number in factors:
    if not (number ** 0.5) % 1 == 0:
        if isSFN(number):
            count += 1

print(count)
