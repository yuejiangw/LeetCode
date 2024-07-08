# 2023-07-30
class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for s in word:
            if s not in curr.children:
                curr.children[s] = Node()
            curr = curr.children[s]
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for s in word:
            if s not in curr.children:
                return False
            curr = curr.children[s]
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for s in prefix:
            if s not in curr.children:
                return False
            curr = curr.children[s]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# 2022-01-26
class Node:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for s in word:
            idx = ord(s) - 97
            if not curr.children[idx]:
                curr.children[idx] = Node()
            curr = curr.children[idx]
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for s in word:
            idx = ord(s) - 97
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for s in prefix:
            idx = ord(s) - 97
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)