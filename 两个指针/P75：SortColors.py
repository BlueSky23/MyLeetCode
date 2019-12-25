# 双指针交换
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        # 初始化下一个应该存储红色和白色的位置
        red = 0 if nums[0] != 0 else 1
        white = 0 if nums[0] != 1 else 1
        if white < red:
            white = red
        i = 1
        while i < len(nums):
            # 将红色交换至应该存储的位置，并更新红色和白色的下一个位置
            if nums[i] == 0:
                # 如果当前位置正好是红色，无需交换
                if i == red:
                    i += 1
                else:
                    nums[i], nums[red] = nums[red], nums[i]
                red += 1
                if white < red:
                    white = red
            elif nums[i] == 1:
                # 如果当前位置正好是白色，无需交换
                if i == white:
                    i += 1
                    white += 1
                    continue
                nums[i], nums[white] = nums[white], nums[i]
                white += 1
            else:
                i += 1
        return nums
