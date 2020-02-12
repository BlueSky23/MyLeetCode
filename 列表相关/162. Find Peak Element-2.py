class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return
        if len(nums) == 1:
            return 0
        # imagine that nums[-1] = nums[n] = -∞
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1

        i, j = 1, len(nums) - 2
        while i <= j:
            mid = (i + j) // 2
            # 总会有解，所以这是出口
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                j = mid - 1
            elif nums[mid] < nums[mid - 1] and nums[mid] > nums[mid + 1]:
                j = mid - 1
            elif nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]:
                i = mid + 1
