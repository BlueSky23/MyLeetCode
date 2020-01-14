class Solution:

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # 从位置(i,j)开始，将连续的‘O’变为‘A’
        def helper(i, j, row, col, board):
            direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            q = [(i, j)]
            while q:
                i, j = q.pop(0)
                board[i][j] = 'A'
                for r, c in direct:
                    if i + r in range(0, row) and j + c in range(0, col):
                        if board[i + r][j + c] == 'O':
                            board[i + r][j + c] = 'A'
                            q.append((i + r, j + c))

        if not board or not board[0]:
            return
        # 获取行、列数
        row, col = len(board), len(board[0])
        # 对所有边缘的O找到相邻O，并暂时置为A
        for i in range(row):
            if board[i][0] == 'O':
                helper(i, 0, row, col, board)
            if board[i][col - 1] == 'O':
                helper(i, col - 1, row, col, board)
        for j in range(col):
            if board[0][j] == 'O':
                helper(0, j, row, col, board)
            if board[row - 1][j] == 'O':
                helper(row - 1, j, row, col, board)
        # 将内部O变为X, 将之前预留的A变回O
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'A':
                    board[i][j] = 'O'
