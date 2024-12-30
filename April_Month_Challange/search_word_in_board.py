class Solution:
    def exist(self, board, word):
        visited = set()
        req = list()
        m = len(board)
        n = len(board[0])

        def bfs(r, c, ptr):
            if r < 0 or r >= m or c < 0 or c >= n :
                return False
            
            if ptr >= len(word):
                return True
            
            if board[r][c] != word[ptr] or (r,c) in visited:
                return False

            visited.add((r,c))
            
            if bfs(r+1, c, ptr+1) or bfs(r, c+1, ptr+1) or bfs(r-1, c, ptr+1) or bfs(r, c-1, ptr+1):
                return True


        for r, row in enumerate(board):
            for c, char in enumerate(board[0]):
                if board[r][c]==word[0]:
                    req.append((r,c))
        
        for cord in req:
            visited.clear()
            if bfs(cord[0], cord[1], 0):
                return True

        return False
                
            
print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "FCEESECBASAD"))
        


"""

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
 
Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 
Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15

["A","B","C","E"],
["S","F","C","S"],
["A","D","E","E"]

word = "ABCB"

"""