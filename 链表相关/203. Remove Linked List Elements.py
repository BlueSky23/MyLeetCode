# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None

        while head:
            if head.val == val:
                head = head.next
            else:
                break

        preNode, curNode = None, head
        while curNode:
            if curNode.val == val:
                if preNode:
                    preNode.next = curNode.next
            else:
                if preNode:
                    preNode.next = curNode
                preNode = curNode

            curNode = curNode.next

        return head