# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return
        # 设置头节点，用于返回
        head = ListNode(-1)
        # 结果链表的游标
        cur = head
        while l1 and l2:
            # 合并L1
            if l1.val < l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            # 合并L2
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
        # 合并剩余元素
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2

        return head.next
