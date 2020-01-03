# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 层次遍历，最后反向输出

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        q = [root]
        ret = []
        while q:
            tmp_val, tmp_node = [], []
            while q:
                node = q.pop(0)
                tmp_val.append(node.val)
                if node.left:
                    tmp_node.append(node.left)
                if node.right:
                    tmp_node.append(node.right)

            q.extend(tmp_node)
            ret.append(tmp_val)

        return ret[::-1]
