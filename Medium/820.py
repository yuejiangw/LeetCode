from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        """
        按照每个单词的逆序构造字典树
        """
        trie = Trie()
        words = [word[::-1] for word in words]
        words = sorted(words, key=len, reverse=True)
        res = 0
        for word in words:
            res += trie.insert(word)
        return res

class Node:
    def __init__(self):
        self.is_word = False
        self.children = [None] * 26
    
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        curr = self.root
        is_new = False
        for s in word:
            idx = ord(s) - 97
            if not curr.children[idx]:
                curr.children[idx] = Node()
                is_new = True
            curr = curr.children[idx]
        curr.is_word = True
        return len(word) + 1 if is_new else 0
