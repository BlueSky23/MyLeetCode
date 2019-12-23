import math

# 纯属技巧，一圈一圈的输出
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return

        num_row, num_col = len(matrix), len(matrix[0])

        rs = []

        idx_row, idx_col = 0, 0
        while idx_row < math.ceil(num_row / 2) and idx_col < math.ceil(num_col / 2):
            # 第一行
            for j in range(idx_col, num_col - idx_col):
                rs.append(matrix[idx_row][j])
            # 最后一列
            for i in range(idx_row + 1, num_row - idx_row):
                rs.append(matrix[i][num_col - idx_col - 1])
            # 最后一行
            if num_row - idx_row - 1 != idx_row:
                for j in range(num_col - idx_col - 2, idx_col - 1, -1):
                    if j > idx_col - 1:
                        rs.append(matrix[num_row - idx_row - 1][j])
            # 第一列
            if idx_col != num_col - idx_col - 1:
                for i in range(num_row - idx_row - 2, idx_row, -1):
                    if i > idx_row:
                        rs.append(matrix[i][idx_col])

            # 继续里面一层
            idx_row += 1
            idx_col += 1

        return rs
