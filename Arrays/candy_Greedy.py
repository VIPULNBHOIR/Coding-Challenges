from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1 for i in range(n)]
        res = 0
        prev = 1

        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                left[i] = prev + 1
                prev += 1
            else:
                prev = 1

        for i in range(n-1,-1,-1):
            if i == n-1:
                res += max(1,left[i])
                prev = 1

            elif ratings[i] > ratings[i+1]:
                res += max( prev + 1, left[i])
                prev += 1
            
            else:
                res += max(1, left[i])
                prev = 1

        return res
print(Solution().candy([1,0,2,3]))
            
        
