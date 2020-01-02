# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 寻找子树的最右节点
        def findMostRight(root):
            while root.right:
                root = root.right
            return root.val

        # 寻找子树的最左节点
        def findMostLeft(root):
            while root.left:
                root = root.left
            return root.val

        if not root:
            return True
        # 叶子节点为真
        bool_left, bool_right = True, True

        # 当前层满足BST的前提下，子树的最大/小值也要满足
        if root.left:
            bool_left = root.val > root.left.val and self.isValidBST(root.left) and findMostRight(root.left) < root.val
        if root.right:
            bool_right = root.val < root.right.val and self.isValidBST(root.right) and findMostLeft(
                root.right) > root.val

        return bool_left and bool_right
