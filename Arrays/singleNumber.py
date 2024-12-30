class Solution:
    def Single_Number(self,nums: list[int]) -> int:
        nums=sorted(nums)
        i=0
        while i < len(nums)-1:
            if (nums[i]!=nums[i+1]):
                break
            else:
                i+=2
        
        return nums[i]


print(Solution().Single_Number([1,2,15,2,1]))


