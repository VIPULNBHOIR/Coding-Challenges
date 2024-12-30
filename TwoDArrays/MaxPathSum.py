class solution():
    def maxsum(self, A: list[int])-> int:
        rows = len(A)
        if rows == 1:
            return max(A[0])

        def bfs(prev_num, i, j):
            if prev_num >= A[i][j]:
                return 0
            
            if i >= rows - 1:
                return A[i][j]
            
            return A[i][j] + max(bfs(A[i][j], i+1, 0), bfs(A[i][j], i+1, 1))

        path1 = A[0][0] + bfs(A[0][0], 1, 0)
        path2 = A[0][0] + bfs(A[0][0], 1, 1)
        path3 = A[0][1] + bfs(A[0][1], 1, 0)
        path4 = A[0][1] + bfs(A[0][1], 1, 1)

        return max(path1, path2, path3, path4)


row = int(input())
A = [list(map(int, input().split())) for _ in range (row)]

print(solution().maxsum(A))


"""

[4,5],
[8,7],
[1,3]

=> 4+8 only

"""