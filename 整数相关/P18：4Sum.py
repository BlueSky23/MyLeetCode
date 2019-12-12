# 基于3sum计算4sum
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 计算threesum
        def threeSum(nums, target):
            if len(nums) < 3:
                return
            # 排序
            nums.sort()
            result = []
            # 取len(nums)-2，是因为至少要凑齐3个元素
            for i in range(len(nums) - 2):
                # 主循环去重
                if i - 1 >= 0 and nums[i] == nums[i - 1]:
                    continue
                temp_value = target - nums[i]
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
                    # 如果最小的两个元素的和也大于目标值，跳过此轮循环
                    if sum(nums[m:m + 2]) > temp_value:
                        break
                    # 如果最大的两个元素的和也小于目标值，跳过此轮循环
                    if sum(nums[-2:]) < temp_value:
                        break
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

        # 基于threesum 计算foursum
        if len(nums) < 4:
            return
        nums.sort()
        result = []
        # len(nums)-3 确保至少4个元素
        for i in range(len(nums) - 3):
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue
            # 如果最小的三个元素的和也大于目标值，跳过此轮循环
            if sum(nums[i + 1:i + 4]) > target - nums[i]:
                continue
            # 如果最大的三个元素的和也小于目标值，跳过此轮循环
            if sum(nums[-3:]) < target - nums[i]:
                continue
            # 求三个元素的和为target-nums[i]
            rs = threeSum(nums[i + 1:], target - nums[i])
            for threesum in rs:
                threesum.append(nums[i])
                result.append(threesum)

        return result


s = Solution()
nums = [1, 0, -1, 0, -2, 2]
print(s.fourSum(nums, 0))
