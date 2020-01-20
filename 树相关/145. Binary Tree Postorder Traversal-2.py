# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return

        ret = []
        stack = []
        # 记录节点是否已被访问过
        s = set()
        while root:
            stack.append(root)
            s.add(root)
            if root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:
                # 更新root，关键的地方，当一条路径遍历到头时，切换root位置
                while stack:
                    tmp = stack.pop(-1)
                    # 如果右节点未被访问，则将游标切换
                    if tmp.right and tmp.right not in s:
                        stack.append(tmp)
                        root = tmp.right
                        break
                    else:
                        ret.append(tmp.val)
                        root = None

        return ret
