# 折半查找，如果找不到，最终得结果一定是a[i]>target,a[j]<target
class Solution:
    def mySqrt(self, x: int) -> int:
        i, j = 0, x
        while i <= j:
            mid = (i + j) // 2
            tmp = mid * mid
            if tmp == x:
                return mid
            elif tmp < x:
                i = mid + 1
            else:
                j = mid - 1
        return j
