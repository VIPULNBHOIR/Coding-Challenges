class Solution(object):

    def largestPerimeter(self, nums):
        long_peri= -1
        for i in range(len(nums)-2):
            large_len=max(nums)
            if ( (sum(nums)-large_len) > large_len ):
                long_peri=sum(nums)
                break
            else:
                nums.remove(large_len)
                
        return long_peri

s=Solution()

# test cases
nums = [5,5,5]
print(s.largestPerimeter(nums))

nums = [1,12,1,2,5,50,3]
print(s.largestPerimeter(nums))

nums = [5,5,50]
print(s.largestPerimeter(nums))

nums = [1,2,3,4,5,6,7]
print(s.largestPerimeter(nums))