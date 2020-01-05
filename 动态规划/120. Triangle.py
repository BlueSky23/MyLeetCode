# 回溯(递归)，超时
# 存在重复计算的子问题，改为动态规划
import sys


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 回溯(递归)
        #         self.minSum=sys.maxsize
        #         def helper(triangle, row, col, pathsum):
        #             # 到最后一行，检查pathsum和已有的最小值
        #             if row==len(triangle)-1:
        #                 if pathsum+triangle[row][col]<self.minSum:
        #                     self.minSum=pathsum+triangle[row][col]
        #                 return
        #             # 将pathsum加上当前值
        #             pathsum+=triangle[row][col]
        #             # # 如果大于已有的最小值，则直接返回
        #             # if pathsum>=self.minSum:
        #             #     return
        #             # 向下两种路径
        #             helper(triangle,row+1,col,pathsum)
        #             helper(triangle,row+1,col+1,pathsum)

        #         helper(triangle,0,0,0)
        #         return self.minSum
        # 动态规划
        # 从低向上计算各个路径的最小值
        dp = list(triangle[-1])
        for i in range(len(triangle) - 2, -1, -1):
            tmp = [0] * (i + 1)
            for j in range(i, -1, -1):
                tmp[j] = min(triangle[i][j] + dp[j], triangle[i][j] + dp[j + 1])
            dp = tmp

        return dp[0]
