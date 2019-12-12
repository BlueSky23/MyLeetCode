class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        cnt = 0
        while cnt < length:
            # 有相同的元素，删除，并更新数组长度
            if cnt - 1 >= 0 and nums[cnt] == nums[cnt - 1]:
                nums.pop(cnt)
                length -= 1
            else:
                cnt += 1
        return length

