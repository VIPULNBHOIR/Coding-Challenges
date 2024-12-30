from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        low = 0
        high = len(nums) - 1
        pos = [-1,-1]
        # for lower bound
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                pos[0] = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        # for upper bound
        low = pos[0] 
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                pos[1] = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return pos

print(Solution().searchRange([5,7,7,8,8,10],8))