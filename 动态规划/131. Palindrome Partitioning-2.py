# 动态规划：时间优，耗空间
# 递归：空间优，耗时间
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 判断是否是回文
        def isPalindrome(s):
            return s == s[::-1]

        if not s:
            return [[]]

        dp = [[] for _ in range(len(s) + 1)]
        dp[len(s)].append([])
        # 由子问题构造父问题
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s) + 1):
                if isPalindrome(s[i:j]):
                    for tmp in dp[j]:
                        dp[i].append([s[i:j]] + tmp)

        return dp[0]
