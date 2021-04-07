# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLength(self, root: ListNode) -> int:
        count = 0
        curr = root
        while curr:
            count += 1
            curr = curr.next
        return count
        
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        length = self.getLength(root)
        result = []
        # 分组数量大于链表长度
        if k > length:
            curr = root
            while curr:
                result.append(ListNode(curr.val))
                curr = curr.next
            result += [ListNode('') for i in range(k - length)]
            return result

        # 分组数量小于等于链表长度
        mod = length % k
        size = length // k
        curr = root
        
        while curr:
            curr_head = curr
            if mod > 0:
                curr_size = size + 1
                mod -= 1
            else:
                curr_size = size
            
            j = 1
            while j < curr_size:
                curr = curr.next
                j += 1
            next_head = curr.next
            curr.next = None
            curr = next_head
            result.append(curr_head)
        return result
            