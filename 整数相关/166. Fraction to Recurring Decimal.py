class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if denominator == 0:
            return
        if numerator == 0:
            return '0'
        # 符号
        sign = ''
        if numerator * denominator < 0:
            sign = '-'
        numerator = abs(numerator)
        denominator = abs(denominator)

        if numerator == denominator:
            return '1'
        # 初始话res
        res = ''
        if numerator > denominator:
            if numerator % denominator == 0:
                res += str(numerator // denominator)
            else:
                res += str(numerator // denominator) + '.'
            numerator = numerator % denominator
        else:
            res = '0.'

        # 已出现过的除数，用于判定是否有循环
        history = {}
        # 记录循环的小数长度
        len_frac = 0
        # 一步步除
        while numerator != 0:
            history[numerator] = len_frac
            # 模仿除法过程
            cnt = 0
            while numerator < denominator:
                numerator *= 10
                cnt += 1
            res += '0' * (cnt - 1)
            len_frac += cnt - 1

            res += str(numerator // denominator)
            len_frac += 1
            numerator = numerator % denominator
            # 除数出现过，则有循环
            if numerator in history:
                ing, frac = res.split('.')
                return sign + ing + '.' + frac[:history[numerator]] + '(' + frac[history[numerator]:] + ')'
        # 除尽
        return sign + res
