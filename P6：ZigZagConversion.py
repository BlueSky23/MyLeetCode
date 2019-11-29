# 利用字符串数组存储每行的字符信息
# 将字符串分段，每段按规律赋值给数组

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        array = [''] * numRows
        step = 2 * numRows - 2

        for i in range(0, len(s), step):
            idx = i
            for j in range(numRows):
                incre = (numRows - j - 1) * 2
                array[j] += s[idx]
                if j > 0 and j < numRows - 1:
                    if idx + incre < len(s):
                        array[j] += s[idx + incre]
                idx += 1
                if idx >= len(s):
                    break

        return "".join(array)
