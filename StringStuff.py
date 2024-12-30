class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        num = list(num)
        i = 0

        while k > 0 and num:
            if i == len(num) - 1 :
                return 0
            
            num1=int(num[i])
            num2=int(num[i+1])
            print(num1, num2)
            if num1 == num2 == 0:
                i += 1
            elif num1 > num2:
                num.pop(i)
                k -= 1
            else:
                num.pop(i+1)
                k -= 1
            
        if not num:
            return 0
        
        num = ''.join(num)
        return int(num)
    


print(Solution().removeKdigits('00858',2))

