class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        lands = set()
        cnt = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in lands:
                    lands.add((i, j))
                    # flooding
                    tmp_list = [(i, j)]
                    while len(tmp_list) > 0:
                        r, c = tmp_list.pop(0)
                        for m, n in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            if r + m in range(rows) and c + n in range(cols):
                                if grid[r + m][c + n] == "1" and (r + m, c + n) not in lands:
                                    tmp_list.append((r + m, c + n))
                                    lands.add((r + m, c + n))
                    cnt += 1

        return cnt
