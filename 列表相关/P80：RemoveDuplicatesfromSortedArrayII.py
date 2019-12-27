class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return
            # 记录某个数字重复次数
        cnt = 1
        # 记录数组索引
        idx = 1
        # 遍历数组
        while idx < len(nums):
            # 是否相同数字
            if nums[idx] == nums[idx - 1]:
                cnt += 1
            else:
                cnt = 1
            # 是否多余两个
            if cnt > 2:
                nums.pop(idx)
            else:
                idx += 1

        return len(nums)