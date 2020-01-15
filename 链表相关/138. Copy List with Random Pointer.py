"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# 思路：先基于next指针生成整个链表的节点，同时保存成顺序列表，方便确认对应的random节点
# 对random指针进行赋值

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return

        new_head = Node(head.val)
        # 用两个列表顺序存储两个链表的节点，方便对应查找random节点
        new_node_list = [new_head]
        old_node_list = [head]
        tmp_old, tmp_new = head, new_head
        random_list = []
        if head.random:
            random_list.append(0)
        cnt = 0
        # 赋值next指针，同时生成new 和 old列表
        while tmp_old.next:
            old_node_list.append(tmp_old.next)
            new_next = Node(tmp_old.next.val)
            new_node_list.append(new_next)
            tmp_new.next = new_next
            # 保存random指针不为空的节点的索引
            cnt += 1
            if tmp_old.next.random:
                random_list.append(cnt)

            tmp_old = tmp_old.next
            tmp_new = tmp_new.next

        # 赋值random指针
        for i in random_list:
            idx = old_node_list.index(old_node_list[i].random)
            new_node_list[i].random = new_node_list[idx]

        return new_head
