# 递归
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 判断是否是回文
        def isPalindrome(s):
            return s == s[::-1]

        if not s:
            return [[]]
        # 递归结束条件
        if len(s) == 1:
            return [[s]]
        # 递归求解子问题
        ret = []
        for i in range(len(s)):
            if isPalindrome(s[:i + 1]):
                tmp = self.partition(s[i + 1:])
                for p in tmp:
                    p[0:0] = [s[:i + 1]]
                    ret.append(p)

        return ret
