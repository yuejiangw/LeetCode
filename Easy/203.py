# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # 头插法建立链表
    def createList(self, nums: List[int]) -> ListNode:
        head = ListNode(None)
        while nums:
            newNode = ListNode(nums.pop(0))
            if head.next == None:
                head.next = newNode
            else:
                newNode.next = head.next
                head.next = newNode
        return head.next

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        curr = head
        tmp = []
        while curr:
            tmp.append(curr.val)
            curr = curr.next
        while val in tmp:
            tmp.remove(val)
        # 因为采用了头插法，所以要倒序构建链表
        return self.createList(tmp[::-1])
