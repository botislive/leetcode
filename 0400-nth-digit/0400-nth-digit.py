class Solution:
    def findNthDigit(self, n: int) -> int:
        base=1
        weight=1
        while n>9*base*weight:
            n-=9*base*weight 
            base+=1
            weight*=10

        ind=(n-1)//base

        target_num=str(weight+ind)
        
        return(int(target_num[(n-1)%base]))   

        
        