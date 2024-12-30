class Solution:
    def Remove_dupli_Two(self, nums):

        counter=1
        actual_i=0
        i=1
        while i < len(nums):

            if(nums[i]==nums[i-1]):
                counter +=1
            else:
                counter =1

            if (counter <= 2):
                actual_i +=1
                nums[actual_i]=nums[i]
            i +=1

        return actual_i +1

print(Solution().Remove_dupli_Two([1,2,2,2,3,4,4]))