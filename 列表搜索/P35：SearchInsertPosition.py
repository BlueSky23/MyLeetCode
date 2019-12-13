# 主要考虑二分法过程中指针的移动过程，如果找不到target且不考虑边界的情况下，
# 有跳出while循环时i>j，且target介于nums[j]和nums[i]之间，所以返回i
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        if target < nums[0]: return 0
        if target > nums[-1]: return len(nums)
        # 二分法
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] > target:
                j = mid - 1
            elif nums[mid] < target:
                i = mid + 1
            else:
                return mid
        # 依据i，j的取值确定target应该的位置
        # target比序列中所有数都大
        # if i>len(nums)-1:
        # return len(nums)
        # target比序列中所有数都小
        # if j<0:
        # return 0
        # 跳出while循环时i>j，且target介于nums[j]和nums[i]之间，所以返回i
        return i
