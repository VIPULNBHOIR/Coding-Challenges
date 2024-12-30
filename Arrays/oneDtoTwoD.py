class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if (m*n != len(original)):
            return "NOT POSSIBLE !!"
        else:
            twoD=[]
            next_ele=0
            for i in range (m):
                twoD.append([ original[ele] for ele in range(next_ele,next_ele + n)])
                next_ele += n
        
        return twoD

print(Solution().construct2DArray([1,2,4,5,4,4],3,2))
