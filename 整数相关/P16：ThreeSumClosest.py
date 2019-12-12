# 思路完全同threeSum题目

class Solution:
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return
            # 排序
        nums.sort()
        # 记录最终返回的和值，以及与target的距离
        result = sum([nums[0], nums[1], nums[2]])
        distance = abs(target - result)
        # 因为最少需要3个元素，所以遍历值len(nums)-2
        for i in range(len(nums) - 2):
            # 双指针相向而行
            m, n = i + 1, len(nums) - 1
            while m < n:
                temp = sum([nums[i], nums[m], nums[n]])
                # 更新为更小的距离值
                if distance > abs(target - temp):
                    distance = abs(target - temp)
                    result = temp
                # 移动m或n，以减小距离值
                if target - temp > 0:
                    m += 1
                elif target - temp < 0:
                    n -= 1
                # 找到最小距离值0，直接返回
                else:
                    return temp
        return result

s = Solution()
print(s.threeSumClosest([0, 1, 2], 0))
