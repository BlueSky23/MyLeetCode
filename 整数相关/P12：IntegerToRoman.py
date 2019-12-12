class Solution:
    def intToRoman(self, num: int) -> str:
        rs = ''
        # 千
        temp = num // 1000
        for i in range(temp):
            rs = rs + 'M'

        # 百
        temp = (num // 100) % 10
        if temp < 4:
            for i in range(temp):
                rs = rs + 'C'
        elif temp == 4:
            rs = rs + 'CD'
        elif temp == 9:
            rs = rs + 'CM'
        else:
            rs = rs + 'D'
            for i in range(temp - 5):
                rs = rs + 'C'

        # 十
        temp = (num // 10) % 10
        if temp < 4:
            for i in range(temp):
                rs = rs + 'X'
        elif temp == 4:
            rs = rs + 'XL'
        elif temp == 9:
            rs = rs + 'XC'
        else:
            rs = rs + 'L'
            for i in range(temp - 5):
                rs = rs + 'X'

        # 个
        temp = num % 10
        if temp < 4:
            for i in range(temp):
                rs = rs + 'I'
        elif temp == 4:
            rs = rs + 'IV'
        elif temp == 9:
            rs = rs + 'IX'
        else:
            rs = rs + 'V'
            for i in range(temp - 5):
                rs = rs + 'I'

        return rs
