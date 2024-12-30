class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        capacity.sort(reverse=True)
        print(capacity)
        total=sum(apple)
        required = 0
        no_of_boxes = 0
        
        for i in capacity:
            required += i
            no_of_boxes += 1
            
            if required >= total:
                break
        
        return no_of_boxes
        


print(Solution().minimumBoxes([1,2,3],[4,3,1,5,2]))