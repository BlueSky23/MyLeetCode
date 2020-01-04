# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(root, sum, path, ret):
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right:
                if root.val == sum:
                    ret.append(list(path))
                path.pop(-1)
                return

            dfs(root.left, sum - root.val, path, ret)
            dfs(root.right, sum - root.val, path, ret)
            path.pop(-1)

        path, ret = [], []
        dfs(root, sum, path, ret)

        return ret
