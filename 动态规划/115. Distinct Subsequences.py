# 用递归超时，存在重复子问题，改用动态规划
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not s:
            return 0
        # 二维数组保持状态，s的后j位和t的后i位有多少种匹配方式
        dp = [[0] * len(s) for _ in range(len(t))]
        # 初始化，t的最后一个字符与s的匹配情况
        cnt = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == t[-1]:
                cnt += 1
            dp[len(t) - 1][i] = cnt
        # 为各种状态赋值
        for i in range(len(t) - 2, -1, -1):
            for j in range(len(s) - 2, -1, -1):
                # 当前字符相同，则匹配时有两种情况，取s[j]和不取s[j]
                if t[i] == s[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i][j + 1]
                # 当前字符不相同
                else:
                    dp[i][j] = dp[i][j + 1]

        return dp[0][0]
