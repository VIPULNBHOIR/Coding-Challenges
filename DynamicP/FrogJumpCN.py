def Minimum(heights, N):
    prev2 = 0
    prev1 = 0
    value2 = value1 = float('inf')

    for pos in range(1, N):
        value1 = prev1 + abs(heights[pos] - heights[pos-1])
        if pos - 2 > -1:
            value2 = prev2 + abs(heights[pos] - heights[pos-2])

        prev2 = prev1
        prev1 = min(value1, value2)
    
    return prev1

n = int(input())

heights = list(int(input()) for _ in range (n)) 

print(Minimum(heights, n))



# its have been more optimised (with SC optimization)

# its required Recursion -> Memoization-> Tabulation-> SC optimization