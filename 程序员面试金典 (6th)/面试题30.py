class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []


    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> None:
        del self.data[-1]

    def top(self) -> int:
        return self.data[-1]

    def min(self) -> int:
        return min(self.data)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()