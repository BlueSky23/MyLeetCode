class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0

        s = s.rstrip()
        size = len(s)
        i = -1
        while i > -size - 1 and s[i] != ' ':
            i -= 1
        return abs(i) - 1