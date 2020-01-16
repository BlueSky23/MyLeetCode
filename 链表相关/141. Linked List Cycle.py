# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow, fast = head, head.next.next
        while fast:
            slow = slow.next
            if not fast.next:
                return False
            fast = fast.next.next
            if slow == fast:
                return True

        return False
