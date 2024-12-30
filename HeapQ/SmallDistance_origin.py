import heapq

class Solution:
    def find(sef,arr,k):
        heap=[]
        result=[]
        for tuple in arr:
            x,y= tuple
            dis= (x*x - y*y)
            print(dis)
            heapq.heappush(heap,[dis,x,y])
        j=0
        while j < k:
            dis,x,y=heapq.heappop(heap)
            arr.insert(0,[x,y])
            j +=1

    
        return arr[0:k]
            

print(Solution().find([[-1,-1],[8,-1],[-5,2],[1,1]],3))
