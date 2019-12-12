# 动态规划实现，为了方便理解，改代码输出最终的最长有效串
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1:
            return 0

        dp = [''] * len(s)
        for i in range(1, len(s)):
            # 扩展一个')''
            if s[i] == ')' and i - len(dp[i - 1]) - 1 >= 0 and s[i - len(dp[i - 1]) - 1] == '(':
                dp[i] = '(' + dp[i - 1] + ')'
                # 与之前的有效串连接
                if dp[i] and i - len(dp[i]) >= 0:
                    dp[i] = dp[i - len(dp[i])] + dp[i]

        maxStr = ''
        for item in dp:
            if len(item) > len(maxStr):
                maxStr = item

        return maxStr


s = Solution()
print(s.longestValidParentheses("(()))())("))
