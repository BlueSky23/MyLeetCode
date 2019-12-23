# 思路：通过不断缩小K来一次确定从高到低的每位数字
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 计算阶乘
        def factorial(n):
            if n == 1:
                return 1
            return n * factorial(n - 1)

        if n <= 0 or k <= 0:
            return

        if k > factorial(n):
            return

        arr = [i for i in range(1, n + 1)]
        ret = ''
        while n > 1:
            # 确定第一位是未排列中的最小值
            if k // factorial(n - 1) == 0:
                m = min(arr)
                arr.remove(m)
                ret += str(m)
                n -= 1
            elif k // factorial(n - 1) > 0:
                tmp = math.ceil(k / factorial(n - 1))
                m = arr[tmp - 1]
                arr.remove(m)
                ret += str(m)
                k = k % factorial(n - 1)
                if k == 0:
                    ret += ''.join([str(i) for i in sorted(arr, reverse=True)])
                    return ret

                n -= 1
        ret += str(arr[0])
        return ret
