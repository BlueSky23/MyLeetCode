# 递归，利用超集概念
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return

        if len(nums) == 1:
            return [[], nums]

        sub = self.subsets(nums[1:])
        ret = []
        for ls in sub:
            tmp = []
            tmp.extend(ls)
            ret.append(tmp)
            ls.append(nums[0])
            ret.append(ls)

        return ret
