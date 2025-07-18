class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cum_sum = 0
        count = 0
        hash = {0: 1}

        for n in nums:
            cum_sum += n
            if cum_sum - k in hash:
                count += hash[cum_sum - k]
            if cum_sum in hash:
                hash[cum_sum] += 1
            else:
                hash[cum_sum] = 1

        return count

        