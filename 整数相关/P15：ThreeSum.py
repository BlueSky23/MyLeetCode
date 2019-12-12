# 双指针，相向而行，根据和与目标值的大小，对应前行
# 特别注意在主循环和次循环中的两次去重
class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return
        # 排序
        nums.sort()
        result = []
        # 取len(nums)-2，是因为至少要凑齐3个元素
        for i in range(len(nums) - 2):
            # 都是正数不可能和为0
            if nums[i] > 0:
                break
            # 主循环去重
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue
            temp_value = 0 - nums[i]
            m, n = i + 1, len(nums) - 1
            while m < n:
                # 去除左边重复元素
                if m > i + 1 and nums[m] == nums[m - 1]:
                    m += 1
                    continue
                # 去除右边边重复元素
                if n < len(nums) - 1 and nums[n] == nums[n + 1]:
                    n -= 1
                    continue

                # 如果两个数和小于需求，需要增大m
                if nums[m] + nums[n] < temp_value:
                    m += 1
                # 如果两个数和大于需求，需要减小n
                elif nums[m] + nums[n] > temp_value:
                    n -= 1
                # 找到满足的三个元素
                else:
                    result.append([nums[i], nums[m], nums[n]])
                    m += 1
                    n -= 1

        return result


s = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(s.threeSum(nums))
