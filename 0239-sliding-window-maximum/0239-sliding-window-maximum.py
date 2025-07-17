import collections
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        j = 0
        out = []
        q = collections.deque()

        while j < len(nums):
            
            while q and nums[q[-1]] < nums[j]:
                q.pop()
            q.append(j)

            
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                out.append(nums[q[0]])

            
                if q[0] == i:
                    q.popleft()

                i += 1
                j += 1

        return out

        
        