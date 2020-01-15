class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                s.remove(nums[i])

        return s.pop()
