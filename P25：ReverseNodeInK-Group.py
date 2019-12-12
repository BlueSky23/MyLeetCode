# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 反转长度为k的链表，返回反转后链表的头节点和尾节点
        def reverseKSize(head, k):
            cnt = 1
            cur = head
            post = cur.next
            while cnt < k:
                tmp = post.next
                post.next = cur
                cur, post = post, tmp
                cnt += 1
            return cur, head
            # 空列表

        if not head:
            return

        last_tail = None
        cnt = 1
        # 待反转子链表的开始节点
        curNode, iterator = head, head
        while iterator.next:
            cnt += 1
            # 找到长度为k的子链表
            if cnt == k:
                # 保存下一个子链表的开始节点
                tmp = iterator.next.next
                # 反转当前子链表
                cur_head, cur_tail = reverseKSize(curNode, k)
                # 与之前反转的子链表连接
                if last_tail:
                    last_tail.next = cur_head
                    last_tail = cur_tail
                else:
                    head = cur_head
                    last_tail = cur_tail
                # 更新下一个子链表的节点信息
                curNode = tmp
                iterator = curNode
                cnt = 1
                # 链表长度是k的整数倍，都反转完了
                if not curNode:
                    break
                continue
            iterator = iterator.next
        # 连接无需反转的剩余节点
        if not last_tail:
            return head
        last_tail.next = curNode

        return head


head = ListNode(1)
tmp = head
for i in range(2, 6):
    tmp.next = ListNode(i)
    tmp = tmp.next

s = Solution()
h = s.reverseKGroup(head, 2)
while h:
    print(h.val)
    h = h.next
