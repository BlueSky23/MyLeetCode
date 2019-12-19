# 思想:取决于利用现有的函数的粒度
# 用一个数组保存每轮乘法的结果
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 用以存储结果的列表
        digits = [0] * (len(num1) + len(num2))
        idx = len(digits) - 1
        # 以较短的数作为主循环
        if len(num1) <= len(num2):
            short, long = num1, num2
        else:
            short, long = num2, num1

        for i in range(len(short) - 1, -1, -1):
            # 按位乘，并更新digits列表
            carry = 0
            cnt = idx
            # 保留进位
            for j in range(len(long) - 1, -1, -1):
                tmp = int(short[i]) * int(long[j]) + carry + digits[cnt]
                local = tmp % 10
                carry = tmp // 10
                digits[cnt] = local
                cnt -= 1
            # 最后的进位
            if carry:
                digits[cnt] = carry

            # 进位，比如第二轮循环从十位开始
            idx -= 1
        # 将digits转为str
        digits = [str(i) for i in digits]
        for i in range(len(digits)):
            if digits[i] != '0':
                rs = ''.join(digits[i:])
                return rs

        return '0'
