class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if not nums:
            return nums
        
        else:
            for num in nums:
                print(num)
                if num == val:
                    nums.remove(num)

                elif num > val:
                    return nums
                
            return nums

        
print(Solution().removeElement([1,2,3,2,5,2,8],2))