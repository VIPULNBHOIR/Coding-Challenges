
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return [-1,-1]  
print(Solution().twoSum([10,20,45,78,12,45], 55))