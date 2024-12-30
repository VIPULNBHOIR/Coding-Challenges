class Solution:
    def CommonSubSeq(self, s1, s2):
        dp = [[-1]*len(s2) for _ in range (len(s1))]

        def f(ind1, ind2):
            if ind1 < 0 or ind2 < 0:
                return 0

            elif dp[ind1][ind2] != -1:
                return dp[ind1][ind2]

            elif s1[ind1] == s2[ind2]:
                dp[ind1][ind2] = 1 + f(ind1- 1, ind2 - 1)
                return dp[ind1][ind2]
            else:
                dp[ind1][ind2] = 0 + max(f(ind1 - 1, ind2), f(ind1, ind2 - 1))
                return dp[ind1][ind2]

        f(len(s1)-1, len(s2)-1)

        return dp[len(s1)-1][len(s2)-1]
        

s1 = str(input())
s2 = str(input())

print(Solution().CommonSubSeq(s1, s2))