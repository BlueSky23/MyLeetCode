class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return

        cnt, size = 0, len(nums)
        while cnt < size:
            if nums[cnt] == val:
                nums.pop(cnt)
                size -= 1
            else:
                cnt += 1
        return size
