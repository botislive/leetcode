class Solution:
    def sortColors(self, nums: List[int]) -> None:
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
        
        # Ensure all keys (0, 1, 2) are present
        dic[0] = dic.get(0, 0)
        dic[1] = dic.get(1, 0)
        dic[2] = dic.get(2, 0)

        count = 0
        for i in range(0, dic[0]):
            nums[count] = 0
            count += 1
        
        for i in range(0, dic[1]):
            nums[count] = 1
            count += 1

        for i in range(0, dic[2]):
            nums[count] = 2
            count += 1
