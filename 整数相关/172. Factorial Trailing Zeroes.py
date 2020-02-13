# 找出n序列中分解出元素5的个数，一个5对应一个0
# 注意，例如30里面有30/5=6个5，会漏掉25分解出来的一个5，所以要加上，依次类推
class Solution:
    def trailingZeroes(self, n: int) -> int:
        res, idx = 0, 0
        # 找出最大的5的指数
        while pow(5, idx) < n:
            idx += 1

        for i in range(1, idx + 1):
            res += n // pow(5, i)

        return res
