import heapq

def LargestRope(arr):
    heapq.heapify(arr)
    cost=lenght=0
    while len(arr) > 1:
        rope1=heapq.heappop(arr)
        rope2=heapq.heappop(arr)

        lenght= rope1 + rope2
        cost += lenght

        heapq.heappush(arr,lenght)
        
    return lenght,cost


print(LargestRope([1,5,4,2,3]))

#O(n) - heapify
#O(log n) - pop
#O(log n) - push


# Overall => nlogn