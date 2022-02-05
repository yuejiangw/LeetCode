# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getNum(self, l: ListNode) -> int:
        if not l:
            return 0
        curr = l
        result = []
        while curr:
            result.append(curr.val)
            curr = curr.next
        result = [str(x) for x in result]
        result = int(''.join(result))
        return result

    def getDigits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        result = []
        while num:
            result.append(num % 10)
            num = num // 10
        return result

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = self.getNum(l1)
        n2 = self.getNum(l2)
        result = n1 + n2
        digits = self.getDigits(result)
        new_head = ListNode()
        for num in digits:
            if new_head.next == None:
                new_head.next = ListNode(num)
            else:
                new_node = ListNode(num)
                new_node.next = new_head.next
                new_head.next = new_node
        return new_head.next
                

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse_list(l: ListNode):
            if not l or not l.next:
                return l
            head = reverse_list(l.next)
            l.next.next = l
            l.next = None
            return head

        p1, p2 = reverse_list(l1), reverse_list(l2)
        carry = 0
        head = ListNode()
        curr = head
        while p1 or p2 or carry:
            num = carry
            if p1:
                num += p1.val
                p1 = p1.next
            if p2:
                num += p2.val
                p2 = p2.next
            curr.next = ListNode(num % 10)
            curr = curr.next
            carry = num // 10

        return reverse_list(head.next)
