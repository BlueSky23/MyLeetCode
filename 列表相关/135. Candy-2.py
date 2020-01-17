# 思路：还是每个元素的糖果数只取决于左右，所以从左向右、从右向左各遍历一次，可得结果
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0

        left2right = [1] * len(ratings)
        right2left = [1] * len(ratings)

        candy = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1] and left2right[i] <= left2right[i - 1]:
                left2right[i] = left2right[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and right2left[i] <= right2left[i + 1]:
                right2left[i] = right2left[i + 1] + 1

        for i in range(len(candy)):
            candy[i] = max(left2right[i], right2left[i])

        return sum(candy)
