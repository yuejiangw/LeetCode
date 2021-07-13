from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRU = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.LRU.keys():
            self.LRU.move_to_end(key)
            return self.LRU[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.LRU) < self.capacity:
            if key in self.LRU.keys():
                self.LRU.move_to_end(key)
                self.LRU[key] = value
            else:
                self.LRU[key] = value
        else:
            if key in self.LRU.keys():
                self.LRU.move_to_end(key)
                self.LRU[key] = value
            else:
                self.LRU.popitem(last=False)
                self.LRU[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)