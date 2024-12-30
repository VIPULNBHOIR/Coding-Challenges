n = int(input().strip())
coins = list(map(int, input().split()))
target = int(input().strip())

total = 0
pt = 0

for i in range(n):
    coin = coins[i]
    total += coin
    if total == target:
        print(pt, i)
        break
    
    elif total < target:
        continue
    else:
        while total > target:
            total -= coins[pt]
            pt += 1
        
        if total == target:
            print(pt, i) 
            break

