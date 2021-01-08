# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getElements(self, l: ListNode) -> List[int]:
        result = []
        curr = l
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result
    
    def getTail(self, l: ListNode) -> ListNode:
        curr = l
        while curr.next:
            curr = curr.next
        return curr

    def getListNodeFromList(self, l: List[int]) -> ListNode:
        if l == []:
            return None
        result = ListNode(None)
        while l:
            target = self.getTail(result)
            target.val = l.pop(0)
            if len(l) == 0:
                break
            target.next = ListNode(None)
        return result

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        e1 = self.getElements(l1)
        e2 = self.getElements(l2)
        tmp = []
        while e1 and e2:
            if e1[0] <= e2[0]:
                tmp.append(e1.pop(0))
            else:
                tmp.append(e2.pop(0))
        tmp += e1
        tmp += e2
        return self.getListNodeFromList(tmp)