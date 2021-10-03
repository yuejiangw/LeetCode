# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List

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