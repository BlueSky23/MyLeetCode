# 注意的python的传值方式
class Solution:
    def permute(self, nums):
        if not nums:
            return
        # 递归结束条件
        if len(nums) == 1:
            return [[nums[0]]]
        # 小问题求解
        tmp = self.permute(nums[1:])
        rs = []
        # 将当前元素插入到所有可能的位置
        for p in tmp:
            for j in range(len(tmp[0])):
                rs.append(p[:j]+[nums[0]]+p[j:])
            rs.append(p+[nums[0]])

        return rs


s = Solution()
print(s.permute([1, 2, 3]))
