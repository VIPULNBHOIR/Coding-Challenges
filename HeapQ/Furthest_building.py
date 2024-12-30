import heapq

def furthestBuilding(heights, bricks, ladders):
    diff_heap = []

    for i in range(len(heights) - 1):
        diff = heights[i + 1] - heights[i]
        if diff > 0:
            heapq.heappush(diff_heap, diff)
            if len(diff_heap) > ladders:
                bricks -= heapq.heappop(diff_heap)
            if bricks < 0:
                return i

    return len(heights) - 1



# Test cases
heights1 = [4, 2, 7, 6, 9, 14, 12]
bricks1, ladders1 = 8, 3
print(furthestBuilding(heights1, bricks1, ladders1))  # Output: 4

heights2 = [4, 12, 2, 7, 3, 18, 20, 3, 19]
bricks2, ladders2 = 10, 2
print(furthestBuilding(heights2, bricks2, ladders2))  # Output: 7

heights3 = [14, 3, 19, 3]
bricks3, ladders3 = 17, 0
print(furthestBuilding(heights3, bricks3, ladders3))  # Output: 3
