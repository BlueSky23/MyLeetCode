# 递归超时，转为动态规划
class Solution:
    def numTrees(self, n: int) -> int:
        if not n:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        # 根据左右子树的节点树进行计算
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 0, 1, 2

        for i in range(3, n + 1):
            # 有一个子树节点数为0
            tmp = 2 * dp[i - 1]
            # 子树节点数都不为0
            for j in range(1, i - 1):
                tmp += dp[j] * dp[i - j - 1]
            dp[i] = tmp

        return dp[n]
