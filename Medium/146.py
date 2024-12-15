from collections import OrderedDict


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        # 双向链表 + 哈希表
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head

    def add(self, node):
        pre_end = self.tail.pre
        pre_end.next = node
        node.pre = pre_end
        node.next = self.tail
        self.tail.pre = node
    
    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def make_recent(self, node):
        # the most recent node is at the tail of the linked list
        # in other words, if we want to remove a node when the cache is at its capacity,
        # we should remove the one at the head
        self.remove(node)
        self.add(node)
    
    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.make_recent(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.make_recent(node)
            return
        
        new_node = ListNode(key, value)
        self.dic[key] = new_node
        self.add(new_node)

        if len(self.dic) > self.capacity:
            node_to_remove = self.head.next
            self.remove(node_to_remove)
            del self.dic[node_to_remove.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

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
        if key not in self.cache and len(self.cache) == self.capacity:
            self.cache.popitem(last=True)
        self.cache[key] = value
        self.cache.move_to_end(key, last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
