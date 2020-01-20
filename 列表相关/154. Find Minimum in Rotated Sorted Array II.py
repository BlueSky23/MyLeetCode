class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return nums[i]

        return nums[0]
