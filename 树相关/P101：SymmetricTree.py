# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 中序遍历，检查结果列表是否对称
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 中序遍历，将值存入队列
        def inOrder(root, queue):
            if root.left:
                inOrder(root.left, queue)
            else:
                queue.append('L')
            queue.append(str(root.val))
            if root.right:
                inOrder(root.right, queue)
            else:
                queue.append('R')

        if not root or (not root.left and not root.right):
            return True
        if not root.left or not root.right or root.left.val != root.right.val:
            return False

        # 遍历并将值存入队列
        q1, q2 = [], []
        inOrder(root.left, q1)
        inOrder(root.right, q2)
        # 检查队列情况，左右互换
        for i in range(len(q1)):
            if q1[i] == 'L':
                q1[i] = 'A'
            elif q1[i] == 'R':
                q1[i] = 'B'

        for i in range(len(q2)):
            if q2[i] == 'L':
                q2[i] = 'B'
            elif q2[i] == 'R':
                q2[i] = 'A'
        # 逆序
        return q1 == q2[::-1]
