# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 非递归前序遍历，利用栈存储相关信息
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        ret = []
        stack = []
        # 遍历当前节点，并将其加入栈，以备后面使用
        while root:
            ret.append(root.val)
            stack.append(root)
            root = root.left
            # 如果当前节点为None，找其父节点的右节点
            if not root:
                while stack:
                    tmp = stack.pop(-1)
                    if tmp.right:
                        root = tmp.right
                        break

        return ret
