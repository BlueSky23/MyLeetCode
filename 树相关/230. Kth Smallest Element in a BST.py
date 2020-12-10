# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def countNodes(root):
            if not root:
                return 0
            return 1 + countNodes(root.left) + countNodes(root.right)

        if not root:
            return None

        tmp = countNodes(root.left)
        if tmp > k - 1:
            return self.kthSmallest(root.left, k)
        elif tmp == k - 1:
            return root.val
        else:
            return self.kthSmallest(root.right, k - tmp - 1)
