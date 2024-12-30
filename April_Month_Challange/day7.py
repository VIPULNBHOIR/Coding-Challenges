class Solution:
    def checkValidString(self, s: str) -> bool:
        
        star_stack = []
        leftP_stack = []

        for i in range(len(s)):
            ele = s[i]
            if ele == '(':
                leftP_stack.append(i)
            elif ele == '*':
                star_stack.append(i)
            else:                      # remove first from "(" stack if not then * stack (if not EMPTY)
                if leftP_stack:
                    leftP_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False

        # if stacks are not EMPTY then
        while leftP_stack and star_stack:
            if leftP_stack[-1] < star_stack[-1]: # check index of '(' is not greater than '*'
                leftP_stack.pop()
                star_stack.pop()
            else:
                return False
            
        #if stack of leftP is not EMPTY then FALSE
        return not leftP_stack


"""Questions

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "((((*))"
Output: true
 

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.


"""