class MinStack:
    """
    空间换时间, 每次入栈一个元组, 表示当前元素的 val 和到当前元素为止的最小值
    这样可以保证 getMin 的时间复杂度为 O(1)
    """
    def __init__(self):
        # Each element in the stack is a typle, represents for (val, min).
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(self.stack[-1][1], val)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
