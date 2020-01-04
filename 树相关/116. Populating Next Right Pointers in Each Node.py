"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


# 递归思想，当前节点左子树的最右节点关联到右子树的最左节点
# 再递归解决子树
class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root or (not root.left and not root.right):
            return root

        left, right = root.left, root.right
        while left:
            left.next = right
            left = left.right
            right = right.left

        self.connect(root.left)
        self.connect(root.right)

        return root
