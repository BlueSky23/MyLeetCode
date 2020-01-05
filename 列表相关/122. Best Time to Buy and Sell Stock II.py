# 见到利润就加
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0
        buy = prices[0]
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                continue
            else:
                if prices[i] > buy:
                    profit += prices[i] - buy
                buy = prices[i + 1]
        # 最后判断一下
        if prices[-1] > buy:
            profit += prices[-1] - buy

        return profit
