class variable:
    def __init__(self, N, grid):
        self.n = N
        self.grid = grid
        self.dp = [[-1]*self.n for _ in range(self.n)]

    def printdp(self):
        for row in self.dp:
            print(row)

class Solution(variable):

    def maxpathSUM(self):
        maxpathsum = float('-inf')

        def isoutbounds(i,j):
            if i >= self.n or j >= self.n:
                return True
            return False

        def pathsum(i,j):
            if isoutbounds(i,j):
                return 0

            if i == self.n -1 and j - self.n - 1:
                return self.grid[i][j]
            
            if self.dp[i][j] != -1:
                return self.dp[i][j]

            self.dp[i][j] = self.grid[i][j] + max(pathsum(i+1, j), pathsum(i, j+1))
            return self.dp[i][j]

        pathsum(0,0)
        return self.dp[0][0]

s = Solution(3, [[4,5,100],[14,6,5],[9,15,10]])

print(s.maxpathSUM())

s.printdp()