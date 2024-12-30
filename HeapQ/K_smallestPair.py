import heapq

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        
        n=len(nums1)

        heap=[]
        leastK_pair=[]

        heapq.heappush(heap,[nums1[0]+nums2[0],0,0])

        while len(leastK_pair) != k:
            print(heap)
            sum,i,j=heapq.heappop(heap)
            leastK_pair.append([sum-nums2[j],nums2[j]])

            if i+1 < n:
                heapq.heappush(heap,[nums1[i+1]+nums2[j],i+1,j])
            if j+1 < n:
                heapq.heappush(heap,[nums1[i]+nums2[j+1],i,j+1])


       
        return leastK_pair

Solution().kSmallestPairs([4,5,6],[1,2,3],5)



# MEDIUM # HEAPQ #ARRAYS # TC= O(k.log(n))
        

