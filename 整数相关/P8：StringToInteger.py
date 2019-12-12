class Solution:
    def myAtoi(self, str: str) -> int:
        dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        # 去除空格
        str = str.strip()

        if not str:
            return 0

        # 获取符号
        sign = 1

        # 获取数字
        valid_str = ''
        idx = 0
        for i in range(len(str)):
            if str[i] in dict:
                valid_str += str[i]
            elif i == 0 and str[i] == '-':
                sign = -1
            elif i == 0 and str[i] == '+':
                pass
            else:
                break
        # 没有有效的数字序列
        if len(valid_str) == 0:
            return 0

        # 值不在合法范围内
        LIMIT = 2 ** 31
        if sign * int(valid_str) < -LIMIT:
            return -LIMIT
        if sign * int(valid_str) > LIMIT - 1:
            return LIMIT - 1

        return sign * int(valid_str)
