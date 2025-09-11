
class StockSpanner:

    def __init__(self):
        self.stack = []
        self.span = []   

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append((price, 1))
            return 1
        res = 1
        while self.stack and price >= self.stack[-1][0]:
            res += self.stack.pop()[1]
        self.stack.append((price, res))
        return res



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)