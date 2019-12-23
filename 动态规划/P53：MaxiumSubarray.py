# 动态规划

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return

        dp = [-1] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i - 1] <= 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i - 1] + nums[i]

        return max(dp)