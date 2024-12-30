from typing import List
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s_data = [0,0] # at index 0 - students with Circuler sandwitch
                       # at index 1 - students with Rectangular sandwitch
        for i in range(len(students)):
            s_shape = students[i]
            if s_shape == 0:
                s_data[0] += 1 
            else:
                s_data[1] += 1

        for sandwich in sandwiches:
            if sandwich == 0:
                if s_data[0] == 0:
                    return s_data[1]
                else:
                    s_data[0] -= 1
            else:
                if s_data[1] == 0:
                    return s_data[0]
                else:
                    s_data[1] -= 1

        return 0



print(Solution().countStudents(students = [1,1,0,0], sandwiches = [1,1,1,1]))



        
        