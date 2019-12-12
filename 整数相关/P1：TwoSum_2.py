class Solution:
    def twoSum(self, nums, target):
        complement = {}
        for i, v in enumerate(nums):
            # if v = nums[i] in complement, we find a solution
            if v in complement:
                return complement[v], i
            # if v = nums[i] not in complement, we store the compliment of the element into the dictionary.
            else:
                complement[target - v] = i
        return -1