class Solution:
    def reverse(self, x: int) -> int:
        # 是0直接返回
        if x == 0:
            return 0
        # 保存符号
        sign = 1
        if x < 0:
            sign = -1
            x = 0 - x
        x = str(x)
        result = sign * int(x[::-1])
        if result < -(2 ** 31) or result > 2 ** 31 - 1:
            return 0

        return result
