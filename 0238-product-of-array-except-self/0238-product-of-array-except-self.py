class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros=nums.count(0)
        product=1
        for n in nums:
            if n!=0:
                product*=n
        if zeros>1:
            return [0]*len(nums)
        
        elif zeros==1:
            return [product if num==0 else 0 for num in nums]
        else:
            return[product//n for n in nums]

        
        