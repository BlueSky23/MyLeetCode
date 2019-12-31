# 动态规划，主要考虑0的特殊性
class Solution:
    def numDecodings(self, s: str) -> int:

        # 特殊情况处理
        if not s or s[0] == '0':
            return 0
        elif len(s) == 1:
            return 1

        # dp[i]表示i之后串的解析方法数
        dp = [0] * len(s)
        # 初始化dp[-1]
        if s[-1] == '0':
            dp[-1] = 0
        else:
            dp[-1] = 1
        # 初始化dp[-2]
        if len(s) >= 2:
            # 以0开始的串都不能解析
            if s[-2] == '0':
                dp[-2] = 0
            else:
                tmp = int(s[-2:])
                if tmp <= 26:
                    if tmp % 10 == 0:
                        dp[-2] = 1
                    else:
                        dp[-2] = 2
                else:
                    if tmp % 10 == 0:
                        dp[-2] = 0
                    else:
                        dp[-2] = 1
        # 顺序向前赋值
        if len(s) > 2:
            for i in range(len(s) - 3, -1, -1):
                if s[i] == '0':
                    dp[i] = 0
                else:
                    tmp = int(s[i:i + 2])
                    if tmp <= 26:
                        if tmp % 10 == 0:
                            dp[i] = dp[i + 2]
                        else:
                            dp[i] = dp[i + 1] + dp[i + 2]
                    else:
                        if tmp % 10 == 0:
                            dp[i] = 0
                        else:
                            dp[i] = dp[i + 1]

        return dp[0]
