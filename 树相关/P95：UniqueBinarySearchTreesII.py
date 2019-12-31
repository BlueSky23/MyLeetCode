# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 树的算法多是递归
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        # n为节点数，val为节点值的最小值
        def helper(n, val):
            if not n:
                return []

            if n == 1:
                node = TreeNode(val)
                return [node]

            ret = []
            # 根据左右子树的节点数分割，同时确定当前节点的值
            for i in range(n):
                tmp1 = helper(i, val)
                tmp2 = helper(n - 1 - i, val + i + 1)

                tmp1 = [None] if not tmp1 else tmp1
                tmp2 = [None] if not tmp2 else tmp2
                # 赋值左右子树
                for p in tmp1:
                    for q in tmp2:
                        node = TreeNode(val + i)
                        node.left = p
                        node.right = q
                        ret.append(node)

            return ret

        return helper(n, 1)



