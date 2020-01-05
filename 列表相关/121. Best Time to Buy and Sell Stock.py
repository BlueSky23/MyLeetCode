# 两次循环计算后一个值减去前面一个值的最大值
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            # 关键的过滤条件，减少解空间
            if prices[i + 1] <= prices[i]:
                continue
            tmp = max(prices[i + 1:]) - prices[i]
            if tmp > profit:
                profit = tmp

        return profit
