# 学习的思路
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        # 最前、最后加一个0元素，方便统一处理
        heights.append(0)
        heights[0:0] = [0]

        stack = [0]
        maxArea = 0
        idx = 1
        while stack and idx < len(heights):
            tmp = stack[-1]
            # 小于栈顶元素，计算栈顶元素为最小值的区域面积
            if heights[idx] < heights[tmp]:
                h = stack.pop(-1)
                if stack:
                    width = idx - stack[-1] - 1
                else:
                    width = idx - h
                    # 栈为空，当前元素最小，入栈
                    stack.append(idx)
                    idx += 1
                maxArea = max(maxArea, heights[h] * width)
            # 大于栈顶元素，入栈
            elif heights[idx] > heights[tmp]:
                stack.append(idx)
                idx += 1
            # 相等不用处理
            else:
                stack[-1] = idx
                idx += 1

        return maxArea
