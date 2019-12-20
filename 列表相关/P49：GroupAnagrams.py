class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            idx = tuple(sorted(s))
            if idx in res:
                res[idx].append(s)
            else:
                res[idx] = [s]

        return [item[1] for item in res.items()]
