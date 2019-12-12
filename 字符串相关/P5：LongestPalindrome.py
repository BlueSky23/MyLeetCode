'''
动态规划思路：
    一个串若两端相同，且中间部分为回文串，则改串为回文串；
    否则，改串的最大回文串为：max{longestPalindrome(s[1:]),longestPalindrome(s[:-1]),longestPalindrome(s[1:-1])}
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s

        if s[0] == s[-1]:
            if s[1:-1] == s[1:-1][::-1]:
                return s

        # 不包含s[0]且以s[-1]结尾的最大回文串
        temp1 = ""
        for i in range(1, len(s)):
            if s[i:] == s[i:][::-1] and len(s[i:]) > len(temp1):
                temp1 = s[i:]
                break
        # 不包含s[-1]且以s[0]开头的最大回文串
        temp2 = ""
        for i in range(len(s) - 1, 0, -1):
            if s[:i + 1] == s[:i + 1][::-1] and len(s[:i + 1]) > len(temp2):
                temp2 = s[:i + 1]
                break
        temp = ""
        if len(temp1) < len(s[1:-1]) and len(temp2) < len(s[1:-1]):
            # 不包含s[0]和s[-1]的最大回文串
            temp = self.longestPalindrome(s[1:-1])

        # 返回长度最大的回文串
        m = max(len(temp), len(temp1), len(temp2))
        if len(temp) == m:
            return temp
        elif len(temp1) == m:
            return temp1
        elif len(temp2) == m:
            return temp2



