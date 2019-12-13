# 思路：首先利用pivot位置的特殊性（比两侧都大，或比两侧都小）二分找到pivot，
# 然后判断target在前半序列还是后半序列，并利用pivot确定待查找的范围
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        # 把序列的最小值作为pivot
        pivot = 0
        left, right = nums[0], nums[len(nums) - 1]
        # 存在rotate，二分找出pivot， O(log(n))
        if left > right:
            i, j = 0, len(nums) - 1
            while i <= j:
                mid = (i + j) >> 1
                # 找到序列的最大值
                if (mid - 1 >= 0 and mid + 1 < len(nums) and nums[mid] > nums[mid - 1] and nums[mid] > nums[
                    mid + 1]) or (mid == 0 and mid + 1 < len(nums) and nums[mid] > nums[mid + 1]):
                    pivot = mid + 1
                    break
                # 找到序列的最小值
                elif (mid - 1 >= 0 and mid + 1 < len(nums) and nums[mid] < nums[mid - 1] and nums[mid] < nums[
                    mid + 1]) or (mid == len(nums) and mid - 1 >= 0 and nums[mid] < nums[mid - 1]):
                    pivot = mid
                    break
                # 移向pivot
                if nums[mid] > left:
                    i = mid + 1
                elif nums[mid] < right:
                    j = mid - 1
        # 无反转
        if left < right:
            i, j = 0, len(nums) - 1
        # 有反转，基于pivot，查找target
        elif target >= nums[0]:
            i, j = 0, pivot - 1
        elif target <= nums[len(nums) - 1]:
            i, j = pivot, len(nums) - 1
        # 二分查找
        while i <= j:
            mid = (i + j) >> 1
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                return mid
        # 没找到
        return -1
