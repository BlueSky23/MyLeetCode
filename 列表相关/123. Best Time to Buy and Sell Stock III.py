# 思路: 学习的方法，正向遍历找到前i天交易一次能够得到的最大收益p，后向遍历找到后j天交易一次能够得到的最大收益q
# 在j>i的情况下，求p[i]+q[j]的最大值

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        # 正向遍历
        p = [0] * len(prices)
        minPrice = prices[0]
        for i in range(1, len(prices)):
            p[i] = max(p[i - 1], prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])

        maxProfit = 0

        # 反向遍历
        q = [0] * len(prices)
        maxPrice = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            q[i] = max(q[i + 1], maxPrice - prices[i])
            maxPrice = max(maxPrice, prices[i])

            maxProfit = max(maxProfit, p[i] + q[i])

        return maxProfit
