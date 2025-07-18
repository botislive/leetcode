from typing import List
import bisect

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        from bisect import bisect_left, insort
        l = 0
        r = 0
        out = []
        window = []

        while r < len(nums):
            # Insert nums[r] into the sorted window
            insort(window, nums[r])

            if r - l + 1 < k:
                r += 1
            elif r - l + 1 == k:
                # Calculate median
                if k % 2 == 1:
                    out.append(float(window[k // 2]))
                else:
                    out.append((window[k // 2] + window[k // 2 - 1]) / 2)

                # Remove nums[l] from the sorted window
                index = bisect_left(window, nums[l])
                del window[index]

                # Slide window
                l += 1
                r += 1

        return out
