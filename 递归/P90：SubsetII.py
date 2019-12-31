class Solution:
    def subsetsWithDup(self, nums):
        if not nums:
            return [[]]
        nums.sort()
        # 转化为子问题求解
        tmp = self.subsetsWithDup(nums[1:])
        # 保存结果
        ret = []
        ret.extend(tmp)
        # 在子问题的每一个解中添加当前元素
        for i in tmp:
            ls = []
            ls.extend(i)
            ls.append(nums[0])
            if ls not in ret:
                ret.append(ls)

        return ret