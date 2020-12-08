class Solution:
    def shortestPalindrome(self, s: str) -> str:
        idx = -1
        for i in range(len(s), 0, -1):
            if s[:i] == s[:i][::-1]:
                idx = i
                break
        return s[idx:][::-1] + s
