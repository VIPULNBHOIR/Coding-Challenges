class Solution:
    def __init__(self, string1):
        self.string1 = string1

    def comsubstring(self):

        m = len(self.string1)
        dp = [[-1]*m for _ in range (m)]
        maxi = 0

        def isPalindrom(i, j):
            if i >= j:
                return True
            
            if dp[i][j] != -1:
                print(f'here for {(i,j)}')
                return True

            if self.string1[i] == self.string1[j]:
                dp[i][j] = isPalindrom(i+1, j-1)
                return dp[i][j]

            return False
                
        
        for i in range(0, m-1):
            for j in range( m-1, i, -1 ):
                if self.string1[i] == self.string1[j]:
                    if isPalindrom(i, j):
                        maxi = max(maxi, j-i + 1)

        print(dp)
        return maxi

text1 = str(input())

s = Solution(text1)

print(s.comsubstring())
