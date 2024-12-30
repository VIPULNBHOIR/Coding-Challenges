from collections import deque

class Solution:
    def maxele(self, array: list[int], k: int)-> list[int]:
        res = []
        queue = deque()
        n = len(array)
        for i in range(k):
            queue.append(array[i])
        res.append(max(queue))

        for i in range(k, n):
            queue.popleft()
            queue.append(array[i])

            res.append(max(queue))
            
        return res

print(Solution().maxele([8,2,5,3,4,9],5))