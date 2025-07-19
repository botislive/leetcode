class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen={}
        for n in nums:
            seen[n]=seen.get(n,0)+1

        for s in seen:
            if seen[s]>len(nums)//2:
                return s


        