class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(k, n, curcomb, allcomb, validlist):
            if k == 1:
                if 1 <= n <= 9 and n not in curcomb:
                    curcomb.append(n)
                    if set(curcomb) not in allcomb:
                        allcomb.append(set(curcomb))
            else:
                if len(validlist) >= k:
                    helper(k - 1, n - validlist[0], curcomb + [validlist[0]], allcomb, validlist[1:])
                    helper(k, n, curcomb, allcomb, validlist[1:])

        curcomb, allcomb = [], []
        validlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        helper(k, n, curcomb, allcomb, validlist)

        return allcomb
