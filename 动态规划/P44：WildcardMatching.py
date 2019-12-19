# 可以转为更小规模的子问题：分治、溯源、动态规划和贪心备选，选择DP
# 状态定义、状态转化、边界条件
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # 至少有一个串为空的情况
        if not s and not p:  # 都匹配完成
            return True
        elif not s and p[0] == '*':  # p未匹配完，但有*
            return self.isMatch(s, p[1:])
        elif not s or not p:  # 有一个已匹配完，但另一个未匹配完，且p不以*开头
            return False

        # 把多个连续的*压缩为一个*
        tmp = p[0]
        for i in range(1, len(p)):
            if p[i] == '*' and p[i] == p[i - 1]:
                continue
            else:
                tmp = tmp + p[i]
        p = tmp

        # 初始化DP数组
        dp = []
        for i in range(len(s)):
            tmp = []
            for j in range(len(p)):
                tmp.append(False)
            dp.append(tmp)

        # 两个串均不为空，赋值最后一元素是否匹配
        if s[len(s) - 1] == p[len(p) - 1] or p[len(p) - 1] == '?' or p[len(p) - 1] == '*':
            dp[len(s) - 1][len(p) - 1] = True
        else:
            dp[len(s) - 1][len(p) - 1] = False

        # 边界赋值
        if len(s) >= 2:
            for i in range(len(s) - 2, -1, -1):
                if p[len(p) - 1] == '*':
                    dp[i][len(p) - 1] = True
                elif p[len(p) - 1] == '?':
                    dp[i][len(p) - 1] = False
                else:
                    dp[i][len(p) - 1] = False
        if len(p) >= 2:
            for j in range(len(p) - 2, -1, -1):
                if p[j] == '*':
                    dp[len(s) - 1][j] = dp[len(s) - 1][j + 1]
                elif p[j] == '?':
                    if p[j + 1] == '*' and j + 1 == len(p) - 1:
                        dp[len(s) - 1][j] = True
                    else:
                        dp[len(s) - 1][j] = False
                else:
                    if p[j + 1] == '*' and j + 1 == len(p) - 1:
                        dp[len(s) - 1][j] = True if s[len(s) - 1] == p[j] else False
                    else:
                        dp[len(s) - 1][j] = False
        # 遍历解决子问题
        if len(s) >= 2 and len(p) >= 2:
            for i in range(len(s) - 2, -1, -1):
                for j in range(len(p) - 2, -1, -1):
                    if p[j] == '*':
                        dp[i][j] = dp[i][j + 1] or dp[i + 1][j]
                    elif p[j] == '?':
                        dp[i][j] = dp[i + 1][j + 1]
                    else:
                        dp[i][j] = dp[i + 1][j + 1] and s[i] == p[j]

        return dp[0][0]