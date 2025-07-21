class Solution:
    def makeFancyString(self, s: str) -> str:
        res = s[0:2] 
        for i in range(2, len(s)):
            if s[i] == res[-1] == res[-2]:
                continue
            res += s[i]
        return res
