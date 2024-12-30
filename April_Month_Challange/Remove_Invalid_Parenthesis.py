class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s=list(s)
        extra = []
        idx = 0
        while idx < len(s):
            char = s[idx]
            if char == '(':
                extra.append(idx)
                idx += 1
            elif char == ')' and extra :
                extra.pop()
                idx += 1
            elif char == ')' and not extra:
                s.pop(idx)
            else:
                idx += 1

        for i in range (len(extra)-1, -1, -1):
            s.pop(extra[i])
            
        return "".join(s)


print(Solution().minRemoveToMakeValid("a(b(c)d)"))
print(Solution().minRemoveToMakeValid("ab(c)d)"))