class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        for j in range(0,len(nums)):
            if nums[j] != 0:
                nums[i]=nums[j]
                i=i+1

        for j in range(i,len(nums)):
            nums[j]=0
        return nums

        