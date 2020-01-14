"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""


# 利用字典建立val和node的关联关系，逐个新建节点并赋值neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        # 用字典建立val和node的索引关系
        dict = {}
        root = Node(node.val, [])
        dict[root.val] = root
        # 采用BFS遍历
        q = [(node, root)]
        while q:
            oldNode, newNode = q.pop(0)
            # 赋值neighbors
            for neighbor in oldNode.neighbors:
                if neighbor.val not in dict:
                    newNeighbor = Node(neighbor.val, [])
                    newNode.neighbors.append(newNeighbor)
                    q.append((neighbor, newNeighbor))
                    dict[newNeighbor.val] = newNeighbor
                else:
                    newNode.neighbors.append(dict[neighbor.val])

        return root
