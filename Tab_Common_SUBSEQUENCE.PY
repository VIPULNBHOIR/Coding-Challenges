class Solution:
    def CommonSubSeq(self, s1, s2):
        M, N = len(s1), len(s2) 
        
        dp = [ [0]*(N + 1) for _ in range (M + 1 ) ]

        for i in range(1,M+1):
            for j in range(1,N+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])


        return dp[M][N]

string1 = str(input().strip())
string2 = str(input().strip())

print(Solution().CommonSubSeq(string1, string2))