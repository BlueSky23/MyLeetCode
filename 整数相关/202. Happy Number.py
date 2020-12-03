class Solution:
    def isHappy(self, n: int) -> bool:

        numbers = set()
        numbers.add(n)

        while n != 1:
            tmp = 0
            while n > 0:
                tmp += pow(n % 10, 2)
                n = n // 10
            if tmp in numbers:
                return False
            numbers.add(tmp)
            n = tmp

        return True