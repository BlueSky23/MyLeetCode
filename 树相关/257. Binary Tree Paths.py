# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def helper(root, s, ls):
            if not root.left and not root.right:
                ls.append(s + '->' + str(root.val))
            else:
                if root.left:
                    helper(root.left, s + '->' + str(root.val), ls)
                if root.right:
                    helper(root.right, s + '->' + str(root.val), ls)

        if not root:
            return []
        ls = []
        if not root.left and not root.right:
            ls.append(str(root.val))
        else:
            if root.left:
                helper(root.left, str(root.val), ls)
            if root.right:
                helper(root.right, str(root.val), ls)
        return ls