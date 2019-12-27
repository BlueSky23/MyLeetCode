# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路：引入一个新链表存储比x大的节点，在原链表删除
# 最后将两个链表连接起来

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return

        tmp = ListNode(x)
        node = tmp

        pre, post = None, head
        while post:
            tmpNode = post.next
            if post.val >= x:
                # 放到后边大的链表中
                node.next = post
                node = post
                node.next = None
                # 在前面的链表中删除
                if pre:
                    pre.next = tmpNode
            else:
                # 更新head为第一个小于x的节点
                if not pre:
                    head = post
                pre = post

            post = tmpNode
        # 将两个链表连接起来
        if pre:
            pre.next = tmp.next
            return head
        else:
            return tmp.next

