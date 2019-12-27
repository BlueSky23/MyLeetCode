# 思路：
# 重点1：DFS在前进的过程中必须沿同一个方向，不然可能构成不可能的回路，比如在本题中，用set存储邻居节点时，取下一个节点的时候顺序不固定，就可能造成回路，得用列表存储，保证顺序一致
# 重点2：回溯当返回False时，注意重置改变得变量值
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(start, board, word, path):
            x, y = start

            # if (x,y) in path:
            #     return False
            if len(word) == 1 and board[x][y] == word:
                return True
            elif len(word) == 1 and board[x][y] != word:
                return False

            path.append((x, y))
            m, n = len(board), len(board[0])

            for i, j in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                if x + i >= 0 and x + i < m and y + j >= 0 and y + j < n:
                    if board[x + i][y + j] == word[1] and (x + i, y + j) not in path:
                        if dfs((x + i, y + j), board, word[1:], path):
                            return True

            path.remove((x, y))
            return False

        # 特殊情况
        if not board or not board[0]:
            return False
        if not word:
            return True
        # 获取首字母的邻居节点信息
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    path = []
                    if len(word) == 1:
                        return True
                    if dfs((i, j), board, word, path):
                        return True

        return False





