# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 遍历列表，存储到数组，利用数组索引删除要求的元素
class Solution:
    def removeNthFromEnd(self, head, n: int):
        tmp_list = []
        node = head
        while node:
            tmp_list.append(node)
            node = node.next
        # 去掉头元素
        if n == len(tmp_list):
            head = head.next
        # 去掉尾元素
        elif n == 1:
            tmp_list[-2].next = None
        # 去掉中间元素
        else:
            tmp_list[-n - 1].next = tmp_list[-n + 1]

        return head