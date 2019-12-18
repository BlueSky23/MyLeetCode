# 有点类似计数排序，利用下标进行查找
class Solution:
    def firstMissingPositive(self, nums) -> int:
        if not nums:
            return 1
        cnt = 0
        while cnt < len(nums):
            # 只对nums[i]小于i+1的元素进行处理，因为大于的并不影响missing的整数
            if nums[cnt] < cnt + 1 and nums[cnt] > 0:
                tmp = nums[cnt] - 1
                # 待交换位置与当前位置元素相等，不处理
                if nums[cnt] == nums[tmp]:
                    cnt += 1
                    continue
                # 待交换位置与当前位置元素不相等，交换，对交换后的元素重新检查
                nums[cnt], nums[tmp] = nums[tmp], nums[cnt]
                continue

            cnt += 1
        # 找出在对应下标处值不对的元素
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1

        return len(nums) + 1