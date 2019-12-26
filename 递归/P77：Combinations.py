# 排列组合的性质：c(k,m)=c(k,m-1)+c(k-1,m-1)
# 注意边界条件
class Solution:
    def combine(self, n: int, k: int):
        if n <= 0 or k <= 0:
            return
        if n < k:
            return

        if k == 1:
            return [[i] for i in range(1, n + 1)]

        if k == n:
            return [[i for i in range(1, n + 1)]]

        tmp1 = self.combine(n - 1, k)
        tmp2 = self.combine(n - 1, k - 1)
        if tmp1 and tmp2:
            for ls in tmp2:
                ls.append(n)
            tmp1.extend(tmp2)

        return tmp1


s = Solution()
print(s.combine(4,2))
