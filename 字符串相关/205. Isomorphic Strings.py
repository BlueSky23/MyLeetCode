class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mappings, mappingt = {}, {}
        for i in range(len(s)):
            if s[i] in mappings:
                if mappings[s[i]] != t[i]:
                    return False
            elif t[i] in mappingt:
                if mappingt[t[i]] != s[i]:
                    return False
            else:
                mappings[s[i]] = t[i]
                mappingt[t[i]] = s[i]

        return True