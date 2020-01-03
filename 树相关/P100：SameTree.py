# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 根据当前节点的状态判断
        if not p and not q:
            return True
        elif not p or not q or p.val != q.val:
            return False

        # 根据左右子节点的状态判断
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)