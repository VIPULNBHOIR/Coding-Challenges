from heapq import heappop , heappush, heapify
class Solution:  
    def kthSmallest(self, matrix, k):
        m, n = len(matrix), len(matrix[0]) 
        maxHeap = []
        for r in range(m):
            for c in range(n):
                heappush(maxHeap, -matrix[r][c])
                print((maxHeap))
                if len(maxHeap)  > k:
                    heappop(maxHeap)
        return -heappop(maxHeap)


matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 5

print(Solution().kthSmallest(matrix,k))


