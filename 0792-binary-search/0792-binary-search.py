class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1   # Move right
            elif nums[mid] > target:
                r = mid - 1   # Move left
            else:
                return mid    # Found target

        return -1  # Not found




        