from typing import List


class Node:
    def __init__(self, val=""):
        self.val = val
        self.is_word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node(c)
            curr = curr.children[c]
        curr.is_word = True

    def in_dict(self, word: str) -> bool:
        curr = self.root
        for c in word:
            curr = curr.children.get(c)
            if not c or not curr.is_word:
                return False
        return True


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        words.sort()
        res = ""
        for word in words:
            trie.insert(word)
            if trie.in_dict(word) and len(word) > len(res):
                res = word
        return res
