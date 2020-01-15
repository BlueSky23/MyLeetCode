class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False

        if s in wordDict:
            return True

        dp = [False] * len(s)
        # 处理最后一位
        if s[-1] in wordDict:
            dp[-1] = True
            # 逐个赋值
        for i in range(len(s) - 2, -1, -1):
            # 如果在dict中，直接为True
            if s[i:] in wordDict:
                dp[i] = True
                continue
            # 否则依次试探，看是否可分
            for j in range(i + 1, len(s)):
                dp[i] = s[i:j] in wordDict and dp[j]
                if dp[i]:
                    break

        return dp[0]
