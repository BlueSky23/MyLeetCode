# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 基于mergeTwoLists实现
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 合并两个有序链表
        def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
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

        if not lists:
            return
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return mergeTwoLists(lists[0], lists[1])

        while len(lists) > 1:
            tmp_lists = []
            # 对lists中的小列表，两两合并
            m, n = 0, len(lists) - 1
            while m < n:
                tmp_lists.append(mergeTwoLists(lists[m], lists[n]))
                m += 1
                n -= 1
            # 元素个数为奇数，剩余一个未合并的
            if m == n:
                tmp_lists.append(lists[m])
            # 更新lists
            lists = tmp_lists
        # lists中只有一个元素，返回
        return lists[0]
