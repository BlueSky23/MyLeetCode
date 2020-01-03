# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 只有两个元素错了，有二种可能
# 1、当前节点的左右子节点交换
# 2、父节点与左子树的最大值或右子树的最小值交换

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # 层次遍历一棵二叉树，获取最大、最小节点值
        def traverse(root):
            min_val, min_node = root.val, root
            max_val, max_node = root.val, root

            q = [root]
            while q:
                node = q.pop(0)
                if node.val > max_val:
                    max_val, max_node = node.val, node
                elif node.val < min_val:
                    min_val, min_node = node.val, node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            return min_node, max_node

        if not root:
            return
        # 找到左右子树的最大/小节点
        if root.left:
            left_max = traverse(root.left)[1]
        if root.right:
            right_min = traverse(root.right)[0]
        # 错误发生在当前节点的左右子树
        if root.left and root.right:
            if left_max.val > right_min.val:
                left_max.val, right_min.val = right_min.val, left_max.val
                return
        # 错误发生在当前节点和左子树
        if root.left:
            if left_max.val > root.val:
                left_max.val, root.val = root.val, left_max.val
                return
        # 错误发生在当前节点和右子树
        if root.right:
            if right_min.val < root.val:
                right_min.val, root.val = root.val, right_min.val
                return
        # 当前层没有错误，检查子树
        if root.left:
            self.recoverTree(root.left)
        if root.right:
            self.recoverTree(root.right)