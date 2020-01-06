class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        # 数字字母集合
        tmp = set()
        l = list(range(97, 123)) + list(range(48, 58))
        for i in l:
            tmp.add(chr(i))
        print(tmp)
        # 从两侧向中间移动判断
        i, j = 0, len(s) - 1
        while i < j:
            while s[i].lower() not in tmp and i < j:
                i += 1
            while s[j].lower() not in tmp and j > i:
                j -= 1
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
                continue
            else:
                return False

        return True
