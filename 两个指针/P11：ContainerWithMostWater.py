# 算法的核心思想，当al<ar时，对任意的l<i<r，一定有Area(al,ar)>Area(al,ai)，即以al为
# 左侧边缘的容器中[al,ar]面积最大，因此可以从解空间中删除所有[al,ai]，从而降低解空间的大小

class Solution:
    def maxArea(self, height) -> int:
        maxArea = 0
        left, right = 0, len(height) - 1
        while left < right:
            # 更新最大容积
            temp = (right - left) * min(height[left], height[right])
            if temp > maxArea:
                maxArea = temp

            # 缩小解空间
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return maxArea
