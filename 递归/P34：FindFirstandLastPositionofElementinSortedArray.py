# 思路：二分查找
# 1，先找到一个target，如果右边有递归查找右边的，如果左边有递归查找左边的
# 2，将左边和右边的查找到的索引和当前索引比较，确定最大和最小
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        # 初始化为-1，-1
        min_idx, max_idx = -1, -1
        # 二分查找
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] > target:
                j = mid - 1
            elif nums[mid] < target:
                i = mid + 1
            else:
                if min_idx == -1:
                    min_idx, max_idx = mid, mid
                    # 递归查找左边部分的target
                    if mid - 1 >= 0 and nums[mid - 1] == target:
                        x1, y1 = self.searchRange(nums[i:mid], target)
                        if x1 != -1 and x1 + i < min_idx:
                            min_idx = x1 + i
                    # 递归查找右边部分的target
                    if mid + 1 < len(nums) and nums[mid + 1] == target:
                        x2, y2 = self.searchRange(nums[mid + 1:j + 1], target)
                        if y2 != -1 and y2 + mid + 1 > max_idx:
                            max_idx = y2 + mid + 1
                break

        return [min_idx, max_idx]
