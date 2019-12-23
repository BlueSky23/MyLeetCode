class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            # 碰到障碍，则后续都不能到达
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for j in range(n):
            # 碰到障碍，则后续都不能到达
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]