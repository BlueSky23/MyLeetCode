# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(root, ret):
            if not root:
                return
            helper(root.left, ret)
            helper(root.right, ret)
            ret.append(root.val)

        ret = []
        helper(root, ret)

        return ret
