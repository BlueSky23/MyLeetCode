class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strlist = []
        for el in zip(*strs):
            if len(set(el)) == 1:
                strlist.append(el[0])
            else:
                break
        return ''.join(strlist)
