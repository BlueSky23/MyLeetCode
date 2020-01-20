# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 合并两个已排好序的链表
        def merge(head1, head2):
            head = ListNode(0)
            tmp = head
            while head1 and head2:
                if head1.val < head2.val:
                    tmp.next = head1
                    head1 = head1.next
                else:
                    tmp.next = head2
                    head2 = head2.next
                tmp = tmp.next
            # 若有剩余，直接附在后面
            if head1:
                tmp.next = head1
            if head2:
                tmp.next = head2

            return head.next

        if not head:
            return
        if not head.next:
            return head

        # 从中间分割，分别排序，再合并
        slow, fast = head, head.next.next
        cnt = 0
        while fast:
            slow = slow.next
            if not fast.next:
                break
            fast = fast.next.next

        tmp = slow.next
        slow.next = None

        rs1 = self.sortList(head)
        rs2 = self.sortList(tmp)
        rs = merge(rs1, rs2)

        return rs