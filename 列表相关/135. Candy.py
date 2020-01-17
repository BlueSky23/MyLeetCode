class Solution:
    def candy(self, ratings: List[int]) -> int:
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