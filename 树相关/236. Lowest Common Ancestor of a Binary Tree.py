# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findParents(root, p, parents):
            if not root:
                return None
            if root == p:
                parents.append(root)
                return parents
            else:
                parents.append(root)
                return findParents(root.left, p, list(parents)) or findParents(root.right, p, list(parents))

        if not root:
            return None
        pparents = findParents(root, p, [])
        qparents = findParents(root, q, [])
        idx = 0
        l = min(len(pparents), len(qparents))
        while idx < l and pparents[idx] == qparents[idx]:
            idx += 1

        return pparents[idx - 1]



