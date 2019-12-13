# 状态：以第i个符号结尾的有效串的长度
# 转移：1、上一个有效串的右侧是），左侧是（；2、当前有效串的左边是另一个独立的有效串
# 初始：dp[1]=0
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        if len(s) <= 1:
            return 0
        dp = [0]
        maxLen = 0
        for i in range(1, len(s)):
            dp.append(0)
            # 扩展一个')''
            if s[i] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - 1] + 2
                # 与之前的有效串连接
                if dp[i] and i - dp[i] >= 0:
                    dp[i] = dp[i - dp[i]] + dp[i]
                if dp[i] > maxLen:
                    maxLen = dp[i]

        return maxLen
