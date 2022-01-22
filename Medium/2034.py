from sortedcontainers import SortedList


class StockPrice:

    def __init__(self):
        self.price = SortedList()
        self.time_price = {}
        self.max_time = 0

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.time_price:
            self.price.remove(self.time_price[timestamp])
        self.time_price[timestamp] = price
        self.price.add(price)
        self.max_time = max(self.max_time, timestamp)

    def current(self) -> int:
        return self.time_price[self.max_time]

    def maximum(self) -> int:
        return self.price[-1]

    def minimum(self) -> int:
        return self.price[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
