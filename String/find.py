class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        s_ = ""
        for letter in range (len(s)-1, -1, -1):
            s_ += s[letter]

        
        for i in range(len(s)-1):
            if s[i: i+2] in s_ :
                return True
        
        return False
            
        
print(Solution().isSubstringPresent( "makertpceket"))

"""Algorithms\

makertpcekt

make the string reverse and find that if two consecutive lrtters are 
present in both the string or not

for EXAMPLE...

if s = makertpceket , hence S_ = "tekecptrekam
therefore "ke" is present in both the string 
Output ="TRUE"

"""