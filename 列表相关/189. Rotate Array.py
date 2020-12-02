class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # temporary list to store values
        idx = [-1] * len(nums)
        for i in range(len(nums)):
            idx[(i + k) % len(nums)] = nums[i]

        # update nums
        for i in range(len(nums)):
            nums[i] = idx[i]
