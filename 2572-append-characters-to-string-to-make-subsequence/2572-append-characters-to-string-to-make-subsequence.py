class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        c1 = 0  
        c2 = 0 

        while c1 < len(s) and c2 < len(t):
            if s[c1] == t[c2]:
                c2 += 1
            c1 += 1

        return len(t) - c2


        