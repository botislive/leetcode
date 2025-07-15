class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic={}
        for n in nums:
            dic[n]=dic.get(n,0)+1
        for key in dic:
            if dic[key]==1:
                return key

        