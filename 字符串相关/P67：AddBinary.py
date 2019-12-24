class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        # 返回值和进位变量
        ret = ''
        carry = 0
        # 按位加
        while i > -1 and j > -1:
            s = int(a[i]) + int(b[j]) + carry
            s, carry = s % 2, s // 2
            ret = str(s) + ret
            i -= 1
            j -= 1
        # a字符串未处理完
        while i > -1:
            s = int(a[i]) + carry
            s, carry = s % 2, s // 2
            ret = str(s) + ret
            i -= 1
        # b字符串未处理完
        while j > -1:
            s = int(b[j]) + carry
            s, carry = s % 2, s // 2
            ret = str(s) + ret
            j -= 1
        # 如果有进位
        if carry:
            ret = str(carry) + ret

        return ret
