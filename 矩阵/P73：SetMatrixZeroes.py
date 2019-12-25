# 思路：不使用额外空间的时候，如果题目要求会对原有数组等变化，可以使用要变化的空间存储临时信息
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 矩阵维度
        m, n = len(matrix), len(matrix[0])

        # 按行标志是否应该为0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][j] = None
                    # 对每行每列设为None，不改变0
                    for k in range(m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = None
                    for k in range(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = None

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == None:
                    matrix[i][j] = 0
