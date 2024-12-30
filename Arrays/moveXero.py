"""class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i=0
        count=len(nums)-1
        while i < count :
            if(nums[i]==0):
                zero=nums.remove(0)
                nums.append(0)
                count -=1
            else:
                i+=1
                
            
        return nums

print(Solution().moveZeroes([0,0,1,0,4,0,2,3,0,3]))"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i=0
        zeros=0
        while i < len(nums) :
            if(nums[i] == 0):
                zeros += 1
            elif (zeros > 0):
                nonZero=nums[i]
                nums[i]=0
                nums[i-zeros]=nonZero

            i += 1
        return nums
                
print(Solution().moveZeroes([1,4,0,0,0,0,2,3,0,3]))