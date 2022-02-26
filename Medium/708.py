"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal, None)
            head.next = head
            return head

        pre, curr = head, head.next
        to_insert = False

        while True:
            # 情况1: 插入的位置在升序链表中
            if pre.val <= insertVal <= curr.val:
                pre.next = Node(insertVal, curr)
                return head
            # 情况2: 插入值大于最大值或者小于最小值, 插入到端点
            elif pre.val > curr.val:
                if insertVal >= pre.val or insertVal <= curr.val:
                    pre.next = Node(insertVal, curr)
                    return head
            
            pre = curr
            curr = curr.next
            if pre == head:
                break
        
        # 情况3: 链表中所有的值都相等, 则直接插入到 head 后
        pre.next = Node(insertVal, curr)
        return head
