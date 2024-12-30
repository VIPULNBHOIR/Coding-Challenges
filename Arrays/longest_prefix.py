class Solution(object):
    
    def longestCommonPrefix(self, strs):
        longest_prefix=""
        first_word=strs[0]

        for i,letter in enumerate (first_word):
            sub_str=first_word[:i+1]
            is_comn=all(word.startswith(sub_str) for word in strs)
            if is_comn:
                longest_prefix=sub_str
            else:
                break

        return longest_prefix

# Test cases
L1 = ['flow', 'flew', 'flower']

L2 = ["dog","racecar","car"]

s=Solution()
print(s.longestCommonPrefix(L1))
print(s.longestCommonPrefix(L2))
