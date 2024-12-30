class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        if m != n:
            return False   

        dictry = {}
        for i in range(m):
            if s[i] != t[i]:
                if s[i] not in dictry:
                    dictry[s[i]] = t[i]
                else:
                    if dictry[s[i]] == t[i]:
                        continue
                    else:
                        return False
        
        return True


print(Solution().isIsomorphic("cut","bah"))
