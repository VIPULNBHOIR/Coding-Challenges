
# 0 1 2 2 2 2 3 3 3 3 5 5

class Solution(object):
    def removeDuplicates(self, nums):
        
        i=1
        actual_i=0
        counter=1

        while i < len(nums):

            if (nums[i] == nums[i-1]):
                counter +=1
            else:
                counter = 1

            if(counter == 1 ):
                actual_i +=1
                nums[actual_i] = nums[i]
                

            i +=1
            
        return actual_i+1
        
print(Solution().removeDuplicates([1,2,2,2,3,4,4,4,4,5,5,6,7,7,7]))

#34 ms runtime

