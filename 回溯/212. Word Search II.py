class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def helper(board, word, idx, starts, positions):
            rows, cols = len(board), len(board[0])
            if idx == len(word) - 1:
                if len(starts) > 0:
                    return True
                else:
                    return False

            b = False
            for i, j in starts:
                tmp = []
                if i - 1 >= 0 and board[i - 1][j] == word[idx + 1] and (i - 1, j) not in positions:
                    tmp.append((i - 1, j))
                if i + 1 < rows and board[i + 1][j] == word[idx + 1] and (i + 1, j) not in positions:
                    tmp.append((i + 1, j))
                if j - 1 >= 0 and board[i][j - 1] == word[idx + 1] and (i, j - 1) not in positions:
                    tmp.append((i, j - 1))
                if j + 1 < cols and board[i][j + 1] == word[idx + 1] and (i, j + 1) not in positions:
                    tmp.append((i, j + 1))
                if len(tmp) > 0:
                    b = b or helper(board, word, idx + 1, tmp, positions + [(i, j)])
            return b

        rs = []
        for word in words:
            starts = []
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == word[0]:
                        starts.append((i, j))
            if helper(board, word, 0, starts, []):
                rs.append(word)

        return rs


