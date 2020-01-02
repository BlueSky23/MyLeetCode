class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 二维数组保持状态
        dp = [[False] * (len(s1) + 1) for _ in range(len(s2) + 1)]
        # 初始化，当s1匹配完后，s2的后半部分是否与s3匹配
        for i in range(len(s2), -1, -1):
            if s2[i:] == s3[i + len(s1):]:
                dp[i][len(s1)] = True
            else:
                break
        # 初始化，当s2匹配完后，s1的后半部分是否与s3匹配
        for i in range(len(s1), -1, -1):
            if s1[i:] == s3[i + len(s2):]:
                dp[len(s2)][i] = True
            else:
                break
        # 逐个赋值
        for i in range(len(s2) - 1, -1, -1):
            for j in range(len(s1) - 1, -1, -1):
                # i个s2的最后元素和j个s1的最后元素对应(i+j)个s3的最后元素，
                if s3[i + j] == s2[i] and s3[i + j] == s1[j]:
                    dp[i][j] = dp[i + 1][j] or dp[i][j + 1]
                elif s3[i + j] == s2[i]:
                    dp[i][j] = dp[i + 1][j]
                elif s3[i + j] == s1[j]:
                    dp[i][j] = dp[i][j + 1]


        return dp[0][0]


s = Solution()
s1 = 'aabcc'
s2 = 'dbbca'
s3 = 'aadbbcbcac'
print(s.isInterleave(s1, s2, s3))
