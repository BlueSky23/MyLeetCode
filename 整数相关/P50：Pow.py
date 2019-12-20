# 分治/折半
# 题目不好，需要判断是否异常
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        if n < -2 ** 31 or n > 2 ** 31 - 1:
            return 0

        sign = 1
        if n < 0:
            sign = -1
            n = -n

        if n % 2 == 0:
            try:
                tmp = self.myPow(x, n / 2)
                tmp = tmp ** 2
            except:
                return 0

        else:
            try:
                tmp = self.myPow(x, (n - 1) / 2)
                tmp = x * tmp ** 2
            except:
                return 0
        if tmp == 0:
            return 0
        return tmp if sign == 1 else 1 / tmp


s = Solution()
print(s.myPow(2.0, -2147483648))
