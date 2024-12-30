import heapq

def last_weight(arr):
    arr=[-i for i in arr]
    heapq.heapify(arr)

    while len(arr) > 1:
        ele1=-1*heapq.heappop(arr)
        ele2=-1*heapq.heappop(arr)

        res_weight=ele1 - ele2
     
        if res_weight >= 0:
            heapq.heappush(arr,-1*res_weight)

    return -1*arr[0]

print(last_weight([2,2]))


#O(n) - making max heap
#O(n) - heapify
#O(logn) - pop
#O(logn) - push


# Overall => nlogn