class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self, head=Node(), tail=None, length=0):
        """
        Initialize your data structure here.
        """
        self.head = head
        self.tail = tail
        self.length = length

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index > self.length - 1:
            return -1
        else:
            curr = self.head.next
            while index > 0:
                curr = curr.next
                index -= 1
            return curr.val


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val, self.head.next)
        self.head.next = new_node
        self.length += 1
        if self.tail is None:
            self.tail = new_node


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.tail is None:
            self.head.next = Node(val)
            self.tail = self.head.next
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        self.length += 1


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index >= 0 and index <= self.length:
            curr = self.head.next
            pre = self.head
            tmp = index
            while tmp > 0:
                pre = curr
                curr = curr.next
                tmp -= 1
            new_node = Node(val, curr)
            pre.next = new_node
            if index == self.length:
                self.tail = new_node
            self.length += 1


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= 0 and index < self.length:
            curr = self.head.next
            pre = self.head
            tmp = index
            while tmp > 0:
                pre = curr
                curr = curr.next
                tmp -= 1
            pre.next = curr.next
            if index == self.length - 1:
                self.tail = pre
            self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)