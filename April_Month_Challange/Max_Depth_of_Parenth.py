class Solution:
    def Max_depth_of_parenth(self, string: str):

        max = 0
        current = 0
        for ele in string:
            if ele == '(':
                current += 1
            elif ele == ')':
                current -= 1

            if max < current :
                max = current

        return max
        
print(Solution().Max_depth_of_parenth("((((((0)))))+(1)+(2)*(((((((2+3))))))))"))

