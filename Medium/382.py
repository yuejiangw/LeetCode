# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import randint
from typing import Optional


class Solution:
    """
    When meeting the i-th element, there should be a probability of 1/i to choose this element,
    a probability of 1 - 1/i to stay the same.

    proof:
    For the i-th element, the probability of choosing it is:
    1/i * (1 - 1/(i+1)) * (1 - 1/(i+2)) * ... * (1 - 1/n) = 1/n
    """

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        i = 0
        res = 0
        curr = self.head
        while curr:
            if randint(0, i) == 0:
                res = curr.val
            i += 1
            curr = curr.next
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
