class Solution(object):
    def firstPalindrome(self, words):
        for word in words:
            if (word == word[::-1]):
                return word

        return ""

s=Solution()

#test cases
words = ["abc","car","ada","racecar","cool"]
print(s.firstPalindrome(words))
words = ["notapalindrome","racecar"]
print(s.firstPalindrome(words))
words = ["def","ghi"]
print(s.firstPalindrome(words))