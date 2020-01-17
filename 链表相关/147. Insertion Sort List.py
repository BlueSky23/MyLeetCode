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
        ordered_list_tail = ordered_list_head
        while head:
            next_node = head.next
            # 此种情况无需与之前元素比较
            if head.val > ordered_list_tail.val:
                ordered_list_tail.next = head
                ordered_list_tail = head
                ordered_list_tail.next = None
                head = next_node
                continue
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
                    ordered_list_tail = head
                    break
                pre, tmp = tmp, tmp.next

            head = next_node

        return ordered_list_head.next
