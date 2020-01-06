class Solution:
    def largestRectangleArea(self, heights) -> int:
        if not heights:
            return 0
        print(len(heights))
        minHeight = min(heights)
        idx = heights.index(minHeight)

        tmp1 = self.largestRectangleArea(heights[:idx])
        tmp2 = self.largestRectangleArea(heights[idx + 1:])

        return max(minHeight * (len(heights)), tmp1, tmp2)


s = Solution()
heights = [2, 1, 5, 6, 2, 3]
print(s.largestRectangleArea(heights))
