class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        frq = []
        count = 0  
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                frq.append(count)
                count = 0
        frq.append(count)  
        return max(frq)


        