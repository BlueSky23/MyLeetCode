class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ''

        # 两个字符串的公共前缀子串
        def longestCommonPrefix(str1, str2):
            rs = ''
            for i in range(len(str1)):
                if i < len(str2) and str1[i] == str2[i]:
                    rs += str1[i]
                else:
                    break
            return rs

        # 逐个遍历数组里的字符串
        rs = strs[0]
        for i in range(1, len(strs)):
            rs = longestCommonPrefix(rs, strs[i])
            if not rs:
                return rs

        return rs
