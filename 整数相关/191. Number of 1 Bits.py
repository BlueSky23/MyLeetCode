class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        idx = 31
        while n > 0:
            tmp = pow(2, idx)
            if n > tmp:
                cnt += 1
                n = n % tmp
            idx -= 1

        return cnt
