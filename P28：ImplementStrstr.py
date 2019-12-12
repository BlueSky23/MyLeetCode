class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        size_needle=len(needle)
        for i in range(len(haystack)-size_needle+1):
            if haystack[i:i+size_needle]==needle:
                return i
        return -1