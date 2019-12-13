# 思路：
# 1、从右往左找第一个逆序对
# 2、找到逆序对中的最小值，并作交换
# 3、交换完成后，再对右边重排序，取最小值
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 从后往前找逆序对
        for i in range(len(nums) - 2, -1, -1):
            tmp = -1
            # 逆序对中的最小值
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    if tmp == -1:
                        tmp = j
                    elif nums[j] < nums[tmp]:
                        tmp = j
            if tmp != -1:
                nums[i], nums[tmp] = nums[tmp], nums[i]
                # 找到最小的逆序对，交换
                for m in range(len(nums) - 1, i + 1, -1):
                    for n in range(i + 1, m):
                        if nums[n] > nums[n + 1]:
                            nums[n], nums[n + 1] = nums[n + 1], nums[n]
                return

        # 没有逆序对，直接反转整个序列
        nums.reverse()
