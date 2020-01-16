# 思路：用回溯存在重复子问题导致超时，改为动态规划
# 仍旧超时，动态规划适用于求最佳解，不适用求全部解
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        if not s:
            return

        dp = [[] for _ in range(len(s))]

        if s[-1] in wordDict:
            dp[-1] = [[s[-1]]]

        for i in range(len(s) - 2, -1, -1):
            # 整个串在wordDict的话，也是一种划分方式
            if s[i:] in wordDict:
                dp[i].append([s[i:]])
            # 向后逐个遍历
            for j in range(i + 1, len(s)):
                if s[i:j] in wordDict:
                    for tmp in dp[j]:
                        dp[i].append([s[i:j]] + tmp)

        ret = []
        for path in dp[0]:
            ret.append(' '.join(path))

        return ret
