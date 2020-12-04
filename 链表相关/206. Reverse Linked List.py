# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # recursively
        if not head or not head.next:
            return head

        tmpNode = self.reverseList(head.next)
        node = tmpNode
        while node.next:
            node = node.next

        node.next = head
        head.next = None

        return tmpNode

        # iteratively
#         if not head or not head.next:
#             return head

#         pre, mid, poster=head, head.next, head.next.next
#         pre.next=None

#         while mid:
#             mid.next=pre
#             pre,mid=mid,poster
#             if poster:
#                 poster=poster.next

#         return pre