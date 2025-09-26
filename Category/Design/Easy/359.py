class Logger:

    def __init__(self):
        self.log = {}


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.log:
            self.log[message] = timestamp 
            return True
        if timestamp - self.log[message] < 10:
            return False
        else:
            self.log[message] = timestamp
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)