class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2,(n-2)+1):
            li=[]
            d=n
            r=0
            q=0
            while d!=0:
                r=d%i
                li.append(r)
                d=d//i
            
            if li !=li[::-1]:
                return False
        return True
            
        