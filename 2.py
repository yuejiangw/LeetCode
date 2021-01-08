# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def getDecimalNum(self, l: ListNode) -> int:
        count = 0
        result = 0
        
        while l != None:
            result += pow(10, count) * l.val
            count += 1
            l = l.next
        return result
    
    def insertNum(self, l: ListNode, val: int) -> ListNode:
        """
        insert val into ListNoe l
        """
        current = l
        while current.next != None:
            current = current.next
        current.next = ListNode()
        current.next.val = val
        current.next.next = None
        return l

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.getDecimalNum(l1)
        num2 = self.getDecimalNum(l2)
        num3 = num1 + num2
        head = ListNode()
        if num3 // 10 == 0:
            head.val = num3
            head.next = None
        else:
            while num3 // 10 != 0:
                head = self.insertNum(head, num3 % 10)
        return head
