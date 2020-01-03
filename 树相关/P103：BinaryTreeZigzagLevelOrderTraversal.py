# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ret = []
        q = [root]
        right = False
        while q:
            tmp_node, tmp_val = [], []
            # 遍历一层
            while q:
                node = q.pop(0)
                tmp_val.append(node.val)
                # 将下一层临时存储到tmp_node中
                if node.left:
                    tmp_node.append(node.left)
                if node.right:
                    tmp_node.append(node.right)
            # 反转
            if right:
                tmp_val = tmp_val[::-1]
            right = not right
            # 更新
            ret.append(tmp_val)
            q.extend(tmp_node)

        return ret
