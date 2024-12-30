class Solution:
    def FindMaxPath(self, matrix, start, end, hurdles):
        n, m = matrix  # Unpack matrix dimensions
        self.maxi = float('-inf')  # Use self.maxi for global maximum tracking
        visited = set()  # To keep track of visited cells

        def dfs(i, j, cost):
            # Check if we have reached the end cell
            if (i, j) == end:
                self.maxi = max(self.maxi, cost)  # Update the maximum path cost if needed
                return

            # Boundary check and hurdles/visited cells
            if i < 0 or i >= n or j < 0 or j >= m or (i, j) in visited or (i, j) in hurdles:
                return

            # Mark the current cell as visited
            visited.add((i, j))

            # Explore all 4 directions with DFS and add to the path cost
            dfs(i, j - 1, cost + 1)  # Left
            dfs(i, j + 1, cost + 1)  # Right
            dfs(i - 1, j, cost + 1)  # Up
            dfs(i + 1, j, cost + 1)  # Down

            # Unmark the cell as visited to allow other paths
            visited.remove((i, j))

        # Start DFS from the start cell with initial cost 0
        dfs(start[0], start[1], 1)

        # Return the result or -1 if no valid path was found
        return self.maxi if self.maxi != float('-inf') else -1

# Input handling
n, m = map(int, input().split())  # Matrix dimensions
h = int(input())  # Number of hurdles
hurdles = set()

for _ in range(h):
    i, j = map(int, input().split())
    hurdles.add((i, j))

# Solution instantiation and method call
result = Solution().FindMaxPath((n, m), (0, 0), (n - 1, m - 1), hurdles)
print("Maximum Path Cost:", result)

