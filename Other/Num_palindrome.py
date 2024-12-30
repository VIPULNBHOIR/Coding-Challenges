class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        y=x[::-1]

        if str(x) == str(y):
            return True
        
        return False
        
s=Solution()
num=int(input())
print(s.isPalindrome(num))

