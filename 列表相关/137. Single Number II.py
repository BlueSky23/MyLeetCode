class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        if not nums:
            return

        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1

        for k in d:
            if d[k] == 1:
                return k
