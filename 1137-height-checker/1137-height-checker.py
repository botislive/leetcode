class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ex=sorted(heights)
        count=0
        for i in range(len(heights)):
            if ex[i] != heights[i]:
                count+=1
        return count


        