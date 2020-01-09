# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路：求事件A，但是需要做事件B，在做事件B的过程中不断获取A

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # 一方面计算以各个节点为根节点的树，包含该节点形成的最大路径和
        # 另一方面，持续更新maxSum
        def dfs(root, maxSum):
            if not root:
                return 0
            # 只有大于0的时候才加进来
            lmax = max(0, dfs(root.left, maxSum))
            rmax = max(0, dfs(root.right, maxSum))
            # 更新maxsum
            maxSum[0] = max(maxSum[0], root.val + lmax + rmax)

            # 返回不以目前节点为根节点且包含该节点的最大路径和
            return max(root.val + lmax, root.val + rmax)

        maxSum = [-sys.maxsize]
        dfs(root, maxSum)

        return maxSum[0]
