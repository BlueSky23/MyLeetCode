# 自己想法：对每个price，从后面的日子里找到最大price，从而计算如果今天买进会收益多少，复杂度是O(n2)
# 学习到的更好方法：反过来，通过记录已遍历数据的最小值，从而计算如果今天卖出会收益多少，复杂度O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        minPrice, profit = prices[0], 0

        for price in prices:
            profit = max(profit, price - minPrice)
            minPrice = min(minPrice, price)

        return profit
