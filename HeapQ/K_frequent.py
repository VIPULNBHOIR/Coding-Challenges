import heapq

def frequent(nums,k):
    if len(nums) == 1:
        return nums

    nums.sort()
    freq=1
    heap=[] #heap
    res=[]
    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]:
            freq +=1
        else:
            heapq.heappush(heap,[-freq,nums[i-1]])
            freq=1
        
        if i == len(nums)-1:
            heapq.heappush(heap,[-freq,nums[i]])

    while k > 0:
        _, num=heapq.heappop(heap)
        res.append(num)
        k -=1

    return res


print(frequent([11,11,11,11,4,4,5,5,8,8,8,1,1,1,1],2))


"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        res = []
        ans = []
        for each in nums:
            cnt[each] = cnt.get(each, 0) + 1
        for ind, value in cnt.items():
            res.append([-value, ind])
        heapq.heapify(res)
        while k > 0:
            ans.append(heapq.heappop(res)[-1])
            k -= 1
        return(ans)
"""

