class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 对角交换
        cnt = n
        for i in range(n):
            for j in range(cnt):
                matrix[i][j], matrix[n - 1 - j][n - 1 - i] = matrix[n - 1 - j][n - 1 - i], matrix[i][j]
            cnt -= 1
        # 上下交换
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]
        return matrix


s = Solution()
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# s.rotate(m)
print(s.rotate(m))
