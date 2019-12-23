class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 验证位置是否有效
        def isValid(boards, x, y):
            n = len(boards)
            # 纵向
            for i in range(x):
                if boards[i][y] == 'Q':
                    return False

            # 左上
            i, j = x, y
            while i > -1 and j > -1:
                if boards[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            # 右上
            i, j = x, y
            while i < n and j > -1:
                if boards[i][j] == 'Q':
                    return False
                i += 1
                j -= 1

            # 左下
            i, j = x, y
            while i > -1 and j < n:
                if boards[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            # 右下
            i, j = x, y
            while i < n and j < n:
                if boards[i][j] == 'Q':
                    return False
                i += 1
                j += 1

            return True

        # 不断发现新的path并加入到res中
        def backtrapping(boards, line, path, res):
            if line == len(boards):
                res.append(path)
                return
            for i in range(n):
                if isValid(boards, line, i):
                    boards[line][i] = 'Q'
                    path.append((line, i))
                    backtrapping(boards, line + 1, path, res)
                    path = path[:line]
                    boards[line][i] = '.'

        # 主循环
        boards = [['.'] * n for _ in range(n)]
        # 每行放一个
        line = 0
        path, res = [], []
        backtrapping(boards, line, path, res)

        rs = []
        for path in res:
            board = []
            for pos in path:
                s = ['.'] * n
                x, y = pos
                s[y] = 'Q'
                board.append(''.join(s))
            rs.append(board)

        return rs
