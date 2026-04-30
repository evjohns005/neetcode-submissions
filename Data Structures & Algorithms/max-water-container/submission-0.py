class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r]) # area is width * the min height
            res = max(res, area) # always recording the max

            # Shift based on the limiting height
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res