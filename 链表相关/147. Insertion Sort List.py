# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return

        ordered_list_head = ListNode(-sys.maxsize)
        while head:
            next_node = head.next
            # 对于每一个元素，在已排好序的列表中插入
            pre, tmp = None, ordered_list_head
            while tmp:
                # 插入中间
                if head.val < tmp.val:
                    head.next = tmp
                    pre.next = head
                    break
                # 插入最后
                if not tmp.next:
                    tmp.next = head
                    head.next = None
                    break
                pre, tmp = tmp, tmp.next

            head = next_node

        return ordered_list_head.next
