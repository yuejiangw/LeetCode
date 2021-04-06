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
                