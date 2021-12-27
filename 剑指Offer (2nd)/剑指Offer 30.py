class Node:
    def __init__(self, val, min, next):
        self.val = val
        self.min = min
        self.next = next


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None

    def push(self, x: int) -> None:
        """ 头插法建立链表，同时更新head的min值 """
        if not self.head:
            self.head = Node(x, x, None)
        else:
            self.head = Node(x, min(self.head.min, x), self.head)

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def min(self) -> int:
        return self.head.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
