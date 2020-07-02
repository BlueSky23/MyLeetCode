# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nodes = []
        temp_node = root
        while temp_node:
            self.nodes.append(temp_node)
            temp_node = temp_node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.hasNext():
            node = self.nodes.pop(-1)
            if node.right:
                temp_node = node.right
                while temp_node:
                    self.nodes.append(temp_node)
                    temp_node = temp_node.left

            return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.nodes) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
