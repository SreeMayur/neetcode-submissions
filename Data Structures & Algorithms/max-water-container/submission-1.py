class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lft = 0
        rgt = len(heights)-1
        water = 0
        while lft < rgt:
            height = min(heights[lft], heights[rgt])
            width = rgt - lft
            area = height * width
            water = max(area, water)
            if heights[lft] < heights[rgt]:
                lft += 1
            else:
                rgt -= 1
        return water