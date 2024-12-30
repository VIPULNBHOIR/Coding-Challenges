class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        total = 0
        no_char = 0
        
        for char in s:
            if char == c:
                no_char += 1
            
        for i in range (no_char, 0, -1):
            total += i
            
        
        return total