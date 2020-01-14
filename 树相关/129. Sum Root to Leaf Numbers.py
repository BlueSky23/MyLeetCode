# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS遍历
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root, sumNum):
            if not root.left and not root.right:
                self.sum += sumNum * 10 + root.val

            sumNum = sumNum * 10 + root.val
            if root.left:
                dfs(root.left, sumNum)
            if root.right:
                dfs(root.right, sumNum)

        if not root:
            return 0

        self.sum = 0
        dfs(root, 0)

        return self.sum
