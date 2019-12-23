# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 思路：先对k进行处理，获取合适的值
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        # 获取链表长度
        length = 0
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next
        # 当k是链表长度的整数倍时，相当于不移动
        k = k % length
        # 两个指针，相隔k＋1，用于最后的指针赋值
        pre, tmp1, tmp2 = None, head, None
        cnt = 0
        while tmp1:
            cnt += 1
            pre = tmp1
            tmp1 = tmp1.next
            if tmp2:
                tmp2 = tmp2.next
            if cnt == k + 1:
                tmp2 = head

        # 更新指针
        pre.next = head
        head = tmp2.next
        tmp2.next = None

        return head