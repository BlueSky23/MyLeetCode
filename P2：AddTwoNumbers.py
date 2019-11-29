# coding=utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        cur = head
        node1, node2 = l1, l2
        increment = 0
        while node1:
            if node2:
                # 计算该位值及进位
                temp_sum = node1.val + node2.val + increment
                increment = int(temp_sum / 10)
                # 生成新节点
                temp_node = ListNode(temp_sum % 10)
                cur.next = temp_node
                cur = temp_node
                # 遍历list 2
                node2 = node2.next
            else:
                # 计算该位值及进位
                temp_sum = node1.val + increment
                increment = int(temp_sum / 10)
                # 生成新节点
                temp_node = ListNode(temp_sum % 10)
                cur.next = temp_node
                cur = temp_node
            # 遍历list 1
            node1 = node1.next
        # list 2比list 1长
        while node2:
            # 计算该位值及进位
            temp_sum = node2.val + increment
            increment = int(temp_sum / 10)
            # 生成新节点
            temp_node = ListNode(temp_sum % 10)
            cur.next = temp_node
            cur = temp_node
            # 遍历list 2
            node2 = node2.next

        if increment:
            temp_node = ListNode(increment)
            cur.next = temp_node
            cur = temp_node

        return head.next
