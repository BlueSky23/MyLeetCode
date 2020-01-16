# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        i, j = 0, len(nodes) - 1
        tmpNode = ListNode(0)
        tmp = tmpNode
        while i < j:
            tmp.next = nodes[i]
            nodes[i].next = nodes[j]
            tmp = nodes[j]
            i += 1
            j -= 1
        if i == j:
            tmp.next = nodes[i]
            nodes[i].next = None
        else:
            tmp.next = None

        return tmpNode.next
