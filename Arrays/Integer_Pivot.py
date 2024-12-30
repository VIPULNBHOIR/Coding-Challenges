import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        nums=[k+1 for k in range(n)]
        mid= math.ceil(len(nums)/2)
        first = sum(nums[0 : mid+1])
        last = sum(nums[mid : n+1])

        while first <= last:
            
            if first == last:
                return nums[mid]

            last -= nums[mid]
            mid += 1
            first += nums[mid]
            

        return -1
        

print(Solution().pivotInteger(17))