from typing import List

class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, s: str):
        curr = self.root
        for c in s:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.is_word = True
    
    def get_prefix_len(self, s: str):
        res = 0
        curr = self.root
        for c in s:
            if c not in curr.children:
                return res
            res += 1
            curr = curr.children[c]
        return res

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        for num in arr1:
            trie.insert(str(num))
        
        res = 0
        for n in arr2:
            res = max(res, trie.get_prefix_len(str(n)))
        return res