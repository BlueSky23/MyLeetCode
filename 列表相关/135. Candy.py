# 核心思想：每个当前元素的糖果数只取决于左右两个元素，逐层迭代更新，直至所有元素都不再变化

class Solution:
    def candy(self, ratings) -> int:
        if not ratings:
            return 0

        # 记录分发糖果个数
        candy = [1] * len(ratings)

        while True:
            flag = False
            # 只关注更新当前元素
            for i in range(len(ratings)):
                # 比较左边
                if i - 1 > -1:
                    if ratings[i] > ratings[i - 1] and candy[i] <= candy[i - 1]:
                        flag = True
                        candy[i] = candy[i - 1] + 1
                # 比较右边
                if i + 1 < len(ratings) and candy[i] <= candy[i + 1]:
                    if ratings[i] > ratings[i + 1]:
                        flag = True
                        candy[i] = candy[i + 1] + 1

            if not flag:
                return sum(candy)


s = Solution()
print(s.candy([1, 2, 3, 3, 1]))
