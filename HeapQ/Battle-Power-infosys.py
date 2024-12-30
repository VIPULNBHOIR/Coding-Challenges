import heapq

class Solution:
    def battle(self, eff: int, power: list[int], bonus: list[int]) -> int:
        heap = []
        cnt = 0
        heapq.heapify(heap)

        for i in range(len(power)):
            heapq.heappush(heap, (power[i], bonus[i]))
        
        for i in range (len(heap)):
            power,bonus = heapq.heappop(heap)
            if power <= eff :
                eff += bonus
                cnt += 1
        
        return cnt


print(Solution().battle(10,[10,20,30,130,50],[100,40,5,0,120]))
