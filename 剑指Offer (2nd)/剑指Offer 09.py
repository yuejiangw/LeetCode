class CQueue:

    def __init__(self):
        self.queue = []

    def appendTail(self, value: int) -> None:
        self.queue.append(value)

    def deleteHead(self) -> int:
        if self.queue == []:
            return -1
        return self.queue.pop(0)


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()