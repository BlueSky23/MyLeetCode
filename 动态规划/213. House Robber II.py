class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(numbs):
            if len(numbs) <= 2:
                return max(numbs)
            dp = [0] * len(numbs)
            dp[0] = numbs[0]
            dp[1] = max(numbs[0], numbs[1])
            for i in range(2, len(dp)):
                dp[i] = max(dp[i - 1], dp[i - 2] + numbs[i])
            return dp[-1]

        if len(nums) <= 3:
            return max(nums)

        return max(nums[0] + helper(nums[2:-1]),
                   nums[1] + helper(nums[3:]),
                   nums[-1] + helper(nums[1:-2]))
