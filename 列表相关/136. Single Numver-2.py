# 利用异或运算，任何数和0做异或等于自身
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]

        return nums[0]