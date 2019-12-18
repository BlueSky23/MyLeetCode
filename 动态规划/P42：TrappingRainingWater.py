# 可以转化成更小规模的子问题，可用动态规划，从底向上给dp数组赋值
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) <= 2:
            return 0

        dp = [0] * len(height)
        for i in range(2, len(height)):
            if height[i] == 0 or height[i] <= height[i - 1]:
                dp[i] = dp[i - 1]
                continue

            m = i - 1
            # 从后向前，找到与cur_height形成存水区的屏障
            for j in range(i - 1, -1, -1):
                # 找到比当前屏障还高的，终止循环
                if height[j] > height[i]:
                    m = j
                    break
                # 找到比当前屏障小的中的最高屏障
                if height[j] > height[m]:
                    m = j

            low = height[i] if height[i] < height[m] else height[m]

            # low和cur_height之间的存水量
            increase = (i - m - 1) * low
            if increase == 0:
                dp[i] = dp[i - 1]
                continue
            # 减去中间的非存水量
            increase -= sum(height[m + 1:i])
            # 子问题存水量与新增量的和
            dp[i] = dp[m] + increase

        return dp[len(height) - 1]