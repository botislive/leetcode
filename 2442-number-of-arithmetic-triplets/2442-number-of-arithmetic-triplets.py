class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen=set(nums)
        counter=0

        for n in nums:
            if n+diff in seen and n+2*diff in seen:
              counter+=1
        return counter
        