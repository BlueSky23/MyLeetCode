# 动态规划
class Solution:
    def minCut(self, s: str) -> int:
        def isPalindrome(s):
            return s == s[::-1]

        if not s or isPalindrome(s):
            return 0
        # 多一位便于统一处理
        dp = [0] * len(s)
        dp.append(-1)
        for i in range(len(s) - 1, -1, -1):
            # 如果是回文，直接处理下一个
            if isPalindrome(s[i:]):
                dp[i] = 0
                continue
            minCut = len(s[i:]) - 1
            for j in range(i + 1, len(s) + 1):
                # 是回文，直接返回1
                if isPalindrome(s[i:j]):
                    if dp[j] == 0:
                        minCut = 1
                        break
                    minCut = min(minCut, 1 + dp[j])
            dp[i] = minCut

        return dp[0]
