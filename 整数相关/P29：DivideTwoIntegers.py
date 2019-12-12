class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1 if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)
        rs = 0
        # 只要被除数不小于除数，结果就会增加
        while dividend >= divisor:
            # 不能用乘除模运算，通过对除数移位操作找到最接近被除数的一个数，对应的cnt也要增加相应倍数
            tmp = divisor
            tmp, cnt = tmp << 1, 1
            while dividend >= tmp:
                cnt = cnt << 1
                tmp = tmp << 1
            # 因为之前的移位操作是tmp大于dividend，所以右移移位复原
            tmp = tmp >> 1
            # 更新被除数，已进行下一轮循环
            dividend -= tmp
            # 更新商值
            rs += cnt

        rs = -rs if sign == -1 else rs
        if rs not in range((-2) ** 31, 2 ** 31):
            return 2 ** 31 - 1
        else:
            return rs


s = Solution()
print(s.divide(10, 3))
