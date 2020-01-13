"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


# 利用中间值作为新的输入

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        # 每一层遍历的其实节点
        levelNode = root

        while levelNode:
            # 每一层遍历的游标节点
            tranverseNode = levelNode
            # 更新下一层遍历的起始节点
            levelNode = None
            # pre和post用于赋值next
            pre, post = None, None
            # 为当前层赋值next
            while tranverseNode:
                # 根据不同情况分别给pre\post\levelNode赋值
                if not tranverseNode.left and not tranverseNode.right:
                    tranverseNode = tranverseNode.next
                    continue
                elif tranverseNode.left and tranverseNode.right:
                    # 更新下一层遍历的起始节点
                    if not levelNode:
                        levelNode = tranverseNode.left
                    if not pre and not post:
                        pre, post = tranverseNode.left, tranverseNode.right
                    else:
                        pre.next = tranverseNode.left
                        pre, post = tranverseNode.left, tranverseNode.right
                elif not tranverseNode.left:
                    # 更新下一层遍历的起始节点
                    if not levelNode:
                        levelNode = tranverseNode.right
                    if not pre:
                        pre = tranverseNode.right
                    else:
                        post = tranverseNode.right
                elif not tranverseNode.right:
                    # 更新下一层遍历的起始节点
                    if not levelNode:
                        levelNode = tranverseNode.left
                    if not pre:
                        pre = tranverseNode.left
                    else:
                        post = tranverseNode.left

                # 更新next指针
                if pre and post:
                    pre.next = post
                    pre = post
                    post = None
                # 移动游标
                tranverseNode = tranverseNode.next

        return root
