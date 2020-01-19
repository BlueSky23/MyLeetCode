# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(root, path):
            path.append(root.val)
            if root.left:
                helper(root.left, path)
            if root.right:
                helper(root.right, path)

        if not root:
            return []

        path = []
        helper(root, path)

        return path
