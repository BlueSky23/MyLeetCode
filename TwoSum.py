# coding=utf-8

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            # 求出目标与当前值的差
            other = target - nums[i]
            pre, post = nums[:i], nums[i + 1:]
            # 判断差在列表的前半部分还是后半部分
            if other in pre:
                return [pre.index(other), i]
            elif other in post:
                return [i, i + 1 + post.index(other)]


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3, 2, 4], 6))
