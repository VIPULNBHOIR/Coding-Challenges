"""
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 
8 is the missing number in the range since it does not appear in nums.

"""
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        expected=n*(n+1)//2 
        actual=sum(nums)

        return expected-actual


print(Solution().missingNumber([0,1,3]))


# time complexity : O(n)
# space complexity : O(1)
