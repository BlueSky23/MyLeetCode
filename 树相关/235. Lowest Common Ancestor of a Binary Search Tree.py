# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        mi, ma = min(p.val, q.val), max(p.val, q.val)
        if mi <= root.val and ma >= root.val:
            return root

        if ma < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif mi > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
