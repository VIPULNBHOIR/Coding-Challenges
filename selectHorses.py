n, k = map(int,input().split())
prices = list(map(int, input().split()))

curr = 0
total = 0
count = 0
maxi = 0

for i in range(n):
    price = prices[i]
    if price >= k :
        curr = i+1
        total = 0
        count = 0
        continue
    else:
        total += price
        count += 1
        if total < k:
            maxi = max(maxi, count)
        else:
            while(total >= k):
                total -= prices[curr]
                curr += 1
                count -= 1

print(maxi)
                
 