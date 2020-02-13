class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return
        if len(nums) == 1:
            return nums[0]

        nums.sort()

        k = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                k += 1
                if k > len(nums) // 2:
                    return nums[i]
            else:
                k = 1
