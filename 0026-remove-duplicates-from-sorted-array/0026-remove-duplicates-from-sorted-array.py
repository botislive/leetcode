class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(i, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1  # ← number of unique elements

        