# 二分查找，先找出pivot，再分别二分查找
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def binarySearch(nums, target):
            if not nums:
                return False
            i, j = 0, len(nums) - 1
            while i <= j:
                mid = (i + j) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    i = mid + 1
                else:
                    j = mid - 1
            return False

        if not nums:
            return False
        pivot = len(nums) - 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                pivot = i - 1
                break

        if target == nums[pivot]:
            return True
        elif target >= nums[0]:
            return binarySearch(nums[:pivot + 1], target)
        else:
            return binarySearch(nums[pivot + 1:], target)
