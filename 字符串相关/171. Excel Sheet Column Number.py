class Solution:
    def titleToNumber(self, s: str) -> int:
        if not s:
            return
            # 每左移一位，增26倍
        idx, res = 0, 0
        for i in range(len(s) - 1, -1, -1):
            res += (ord(s[i]) - 64) * pow(26, idx)
            idx += 1

        return res
