class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        
        output= 0
        happiness.sort(reverse = True)
        i = 0
        minus_pointer = 0
        
        while k > 0 and len(happiness) > 0:
            
            if (happiness[i] - minus_pointer) <= 0 :
                output += 0
                
            else:
                output += (happiness[i] - minus_pointer)
                minus_pointer += 1
                
            k -= 1   
            happiness.pop(0)
        
        return output

              
                
            