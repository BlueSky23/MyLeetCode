class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        diff = nums[1] - nums[0]
        for i in range(2, len(nums)):
            diff = max(diff, nums[i] - nums[i - 1])

        return diff
