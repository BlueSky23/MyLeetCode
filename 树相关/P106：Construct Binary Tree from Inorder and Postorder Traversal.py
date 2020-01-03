# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return
        root = TreeNode(postorder[-1])
        # 生成左右子树的postorder和inorder列表
        idx = inorder.index(postorder[-1])

        # 递归生成左右子树
        left = self.buildTree(inorder[:idx], postorder[:idx])
        right = self.buildTree(inorder[idx + 1:], postorder[idx:-1])

        root.left, root.right = left, right

        return root
