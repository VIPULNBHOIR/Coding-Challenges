class Solution:
    def Build_String(self, s: str) -> str:
        if len(s) < 2 : return s
        ptr1=0
        ptr2=1
        s = list(s)

        while len(s) != 0 and ptr1 < len(s)-1:
            
            if ptr1 < 0 and ptr2 < 1:
                    ptr1 = 0
                    ptr2 = 1

            cond1 = s[ptr1].lower() == s[ptr2] and s[ptr2].upper() == s[ptr1] 
            cond2 = s[ptr1].upper() == s[ptr2] and s[ptr2].lower() == s[ptr1] 
            
            if cond1 or cond2:
                s.pop(ptr2)
                s.pop(ptr1) 
                ptr1 -= 1
                ptr2 -= 1

            else:
                ptr1 += 1
                ptr2 += 1

            
        return ''.join(s)

print(Solution().Build_String("LEelTcCtoEdDeO"))
print(Solution().Build_String("SjhjEwWeYyeE"))


"""

if Ee OR eE,  remove both because small_capital OR Capital_small 
hence LlTcCtoEdDeO

again Ll, remove both
hence cCtoEdDeO

hence cC remove
hence toEdDeO

finally... OUTPUT = ""

"""