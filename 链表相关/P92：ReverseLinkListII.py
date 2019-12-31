# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return
        if m == n:
            return head

        cnt = 0
        node = head
        pre, post = None, None
        h, t = None, None
        flag = False
        while node:
            cnt += 1
            # 反转
            if flag:
                tmp = node.next
                node.next = h
                h = node
                node = tmp
                # 保存后一个节点
                if cnt == n:
                    post = node
                    break
            # 寻找反转起始点
            else:
                # 保存前一个节点
                if cnt == m:
                    h = node
                    t = node
                    flag = True
                else:
                    pre = node

                node = node.next
        # 链接起来
        if pre:
            pre.next = h
            t.next = post
            return head
        else:
            t.next = post
            return h


ln1 = ListNode(3)
ln2 = ListNode(5)
ln1.next = ln2
s = Solution()
h = s.reverseBetween(ln1, 1, 2)
while h:
    print(h.val)
    h = h.next
