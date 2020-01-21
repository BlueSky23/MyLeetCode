# 思路：关键时处理负数的情况

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return
        # 记录前一个负值，处理负数的情况
        stack = []
        # 保留以nums[i]结尾的最大乘积值
        dp = [1] * len(nums)
        dp[0] = nums[0]
        neg = 1
        if nums[0] < 0:
            stack.append(nums[0])

        for i in range(1, len(nums)):
            # 0 把数列分为多段，每段的最大值即为最终的最大值
            if nums[i] == 0:
                dp[i] = 0
                stack = []
                neg = 1
            # 考虑前面有几个负值，计算当前的最大值
            elif nums[i] < 0:
                if not stack:
                    dp[i] = 0 if dp[i - 1] == 0 else nums[i]
                    if dp[i - 1] == 0:
                        stack.append(nums[i])
                    else:
                        stack.append(nums[i] * dp[i - 1])
                elif len(stack) == 1:
                    if dp[i - 1] > 0:
                        dp[i] = stack[0] * dp[i - 1] * nums[i]
                    else:
                        dp[i] = stack[0] * nums[i]
                    stack.append(dp[i])
                else:
                    if neg < 0:
                        dp[i] = neg * nums[i] * stack[1]
                    else:
                        dp[i] = neg * nums[i] * int(stack[1] / stack[0])
                    neg *= nums[i]
            else:
                dp[i] = nums[i] * dp[i - 1] if dp[i - 1] > 0 else nums[i]
                if len(stack) >= 2:
                    neg *= nums[i]

        return max(dp)
