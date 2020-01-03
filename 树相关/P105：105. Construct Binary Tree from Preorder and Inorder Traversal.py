# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder and not inorder:
            return
        # 生成当前节点
        root = TreeNode(preorder[0])
        # 生成左右子树的preorder和inorder列表
        idx = inorder.index(preorder[0])
        # left_inorder=inorder[:idx]
        # right_inorder=inorder[idx+1:]
        # left_preorder=preorder[1:len(left_inorder)+1]
        # right_preorder=preorder[len(left_inorder)+1:]

        # 递归生成左右子树
        left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])

        root.left, root.right = left, right

        return root
