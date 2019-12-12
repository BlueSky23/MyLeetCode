# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return

        pre, left, right = None, head, head.next
        while left and right:
            # 交换相邻的节点
            left.next = right.next
            right.next = left
            if pre:
                pre.next = right
            else:  # 交换第一对，更新head节点
                head = right
            # 更新节点
            pre = left
            if left.next and left.next.next:
                left = pre.next
                right = pre.next.next
            else:
                break

        return head
