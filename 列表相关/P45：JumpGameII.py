# 思路：单源最短路径
class Solution:
    def jump(self, nums) -> int:

        if not nums:
            return
        if len(nums) == 1:
            return 0
        # 存储已到达过的位置
        tmp = [0]
        # 从0到某个位置所需的跳数
        dp = [-1] * len(nums)
        dp[0] = 0
        while tmp:
            idx = tmp.pop(0)
            for i in range(nums[idx], 0, -1):
                if idx + i >= len(nums) - 1:
                    return dp[idx] + 1
                # 没到达过
                if dp[idx + i] == -1:
                    tmp.append(idx + i)
                    dp[idx + i] = dp[idx] + 1

        return dp[len(nums) - 1]


s = Solution()
n = [6, 2, 6, 1, 7, 9, 3, 5, 3, 7, 2, 8, 9, 4, 7, 7, 2, 2, 8, 4, 6, 6, 1, 3]
print(s.jump(n))
