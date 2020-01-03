# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        # 取中间元素
        idx = len(nums) // 2
        root = TreeNode(nums[idx])
        # 递归实现左右子树
        left = self.sortedArrayToBST(nums[:idx])
        right = self.sortedArrayToBST(nums[idx + 1:])

        root.left, root.right = left, right

        return root
