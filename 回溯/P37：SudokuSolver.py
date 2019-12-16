class Solution:
    # 找到当前位置(i,j)可能的取值范围
    def get_possible_pos(self, board, i, j):
        temp = set()
        for k in range(9):
            # 行
            if board[i][k] != '.':
                temp.add(board[i][k])
            # 列
            if board[k][j] != '.':
                temp.add(board[k][j])
        # 3*3
        x_idx, y_idx = i // 3, j // 3
        x_idx, y_idx = x_idx * 3, y_idx * 3
        for m in range(x_idx, x_idx + 3):
            for n in range(y_idx, y_idx + 3):
                if board[m][n] != '.':
                    temp.add(board[m][n])
                    # 数字全集
        digits = set()
        digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        # 做差求出可能的取值范围
        rs = digits.difference(temp)
        if rs:
            return list(rs)
        else:
            return None

    # 获取下一个需要设置值的位置
    def get_next_pos(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    return i, j
        return None

    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        next_pos = self.get_next_pos(board)
        # 都放满了
        if not next_pos:
            return True

        i, j = next_pos
        # 当前的位置没有可放的数字
        if not self.get_possible_pos(board, i, j):
            return False
        for digit in self.get_possible_pos(board, i, j):
            # 设置当前位置的数字
            board[i][j] = digit
            # 更新当前位置后，递归求解后续的数独问题
            if self.solveSudoku(board):
                return True
            # 恢复当前状态，考虑for循环的最后一个，如果不重置，会保留一个错误状态
            board[i][j] = '.'

        return False


s = Solution()
input = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# i, j = s.get_next_pos(input)
# print(i, j)
# print(s.get_possible_pos(input, i, j))
s.solveSudoku(input)
print(input)
