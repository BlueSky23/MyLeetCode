class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return
        # 递归结束条件
        if len(nums) == 1:
            return [[nums[0]]]
        # 小问题求解
        tmp = self.permuteUnique(nums[1:])
        rs = []
        # 将当前元素插入到所有可能的位置
        for p in tmp:
            for j in range(len(tmp[0])):
                tmp_permutation = p[:j] + [nums[0]] + p[j:]
                if tmp_permutation not in rs:
                    rs.append(tmp_permutation)
            if p + [nums[0]] not in rs:
                rs.append(p + [nums[0]])

        return rs
