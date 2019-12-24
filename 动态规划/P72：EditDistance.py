class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 递归终止条件
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1 == word2:
            return 0
        # 动态规划，保存从0到i位和从0到j位需要的操作数
        dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]

        for j in range(len(word1) + 1):
            dp[0][j] = j
        for i in range(len(word2) + 1):
            dp[i][0] = i

        for i in range(len(word2)):
            for j in range(len(word1)):
                if word1[j] == word2[i]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1

        return dp[len(word2)][len(word1)]
