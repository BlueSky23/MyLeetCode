class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # method 1
        # return len(nums)!=len(list(set(nums)))
        # method 2
        s = dict()
        for n in nums:
            if n in s:
                return True
            else:
                s[n] = 1

        return False