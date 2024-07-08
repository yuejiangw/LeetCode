from collections import OrderedDict


class LRUCache:
    """
    要求 get 和 put 的时间复杂度都是 O(1)，则需要用 LinkedHashMap
    若是自己实现，则首先需要一个双向链表，对于其中的每个节点，需要存储 key, val, pre, next
    之后还要一个哈希表，存储 key 和对应的 node，这样我们就可以利用哈希表实现 O(1)
    """

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def make_recent(self, key):
        self.cache.move_to_end(key, last=False)

    def get(self, key: int) -> int:
        if key in self.cache:
            self.make_recent(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.make_recent(key)
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem()
            self.cache[key] = value
            self.make_recent(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
