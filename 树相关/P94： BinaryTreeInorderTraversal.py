# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 树的中序遍历

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def traversal(root, ret):
            if root.left:
                traversal(root.left, ret)
            ret.append(root.val)
            if root.right:
                traversal(root.right, ret)

        if not root:
            return

        ret = []
        traversal(root, ret)

        return ret
