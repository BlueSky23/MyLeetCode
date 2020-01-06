# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def getHeight(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            return 1 + max(getHeight(root.left), getHeight(root.right))

        if not root:
            return True

        left = getHeight(root.left)
        right = getHeight(root.right)

        if abs(left - right) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
