class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        primes = [True] * (n - 1)
        primes[0] = False

        for i in range(2, ceil(sqrt(n))):
            if primes[i - 1]:
                for j in range(i * i, n, i):
                    primes[j - 1] = False

        cnt = 0
        for prime in primes:
            if prime:
                cnt += 1

        return cnt