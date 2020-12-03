# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        vals = []
        parents_num, children_num = 1, 0
        nodes = [root]
        while len(nodes) != 0:
            node = nodes.pop(0)
            parents_num -= 1

            if node.left:
                nodes.append(node.left)
                children_num += 1
            if node.right:
                nodes.append(node.right)
                children_num += 1

            if parents_num == 0:
                vals.append(node.val)
                parents_num = children_num
                children_num = 0

        return vals
