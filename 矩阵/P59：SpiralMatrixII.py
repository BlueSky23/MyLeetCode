import math


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n <= 0:
            return
        matrix = [[0] * n for _ in range(n)]
        idx_row, idx_col = 0, 0
        val = 1
        while idx_row <= math.ceil(n / 2) and idx_col < math.ceil(n / 2):
            for j in range(idx_col, n - idx_col):
                matrix[idx_row][j] = val
                val += 1
            for i in range(idx_row + 1, n - idx_row - 1):
                matrix[i][n - idx_col - 1] = val
                val += 1

            if n - idx_row - 1 != idx_row:
                for j in range(n - idx_col - 1, idx_col - 1, -1):
                    matrix[n - idx_row - 1][j] = val
                    val += 1
            if idx_col != n - idx_col - 1:
                for i in range(n - idx_row - 2, idx_row, -1):
                    matrix[i][idx_col] = val
                    val += 1

            idx_row += 1
            idx_col += 1

        return matrix