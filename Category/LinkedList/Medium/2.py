# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 纯指针操作
        dummy_head = ListNode()
        curr = dummy_head
        p1, p2 = l1, l2
        carry = 0
        while p1 and p2:
            val = p1.val + p2.val
            curr.next = ListNode((val + carry) % 10)
            carry = (val + carry) // 10
            p1 = p1.next
            p2 = p2.next
            curr = curr.next
        while p1:
            val = p1.val
            curr.next = ListNode((val + carry) % 10)
            carry = (val + carry) // 10
            p1 = p1.next
            curr = curr.next
        while p2:
            val = p2.val
            curr.next = ListNode((val + carry) % 10)
            carry = (val + carry) // 10
            p2 = p2.next
            curr = curr.next
        if carry != 0:
            curr.next = ListNode(carry)
        return dummy_head.next

class Solution:
    def getNum(self, l: ListNode) -> int:
        curr = l 
        result = 0
        i = 0
        while curr != None:
            result += curr.val *  pow(10, i)
            curr = curr.next
            i += 1
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
        num1 = self.getNum(l1)
        num2 = self.getNum(l2)
        num = num1 + num2
        digits = self.getDigits(num)
        result = ListNode(None)
        curr = result
        while digits:
            curr.val = digits.pop(0)
            if digits == []:
                return result
            else:
                curr.next = ListNode(None)
                curr = curr.next