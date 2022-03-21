class Node:
    def __init__(self):
        self.words = [None for _ in range(26)]
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not curr.words[idx]:
                curr.words[idx] = Node()
            curr = curr.words[idx]
        curr.is_word = True
    
    def search(self, prefix):
        curr = self.root
        res = []
        path = []
        for char in prefix:
            idx = ord(char) - ord('a')
            child = curr.words[idx]
            if not child:
                return []
            else:
                path.append(char)
                curr = child

        def backtracking(root):
            if not root:
                return
            if root.is_word:
                res.append(''.join(path))
                if len(res) == 3:
                    return
            for i in range(26):
                if root.words[i] is not None:
                    char = chr(ord('a') + i)
                    path.append(char)
                    if len(res) == 3:
                        break
                    backtracking(root.words[i])
                    path.pop()
        
        backtracking(curr)
        return res

            
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # T: O(sum(L) + S)
        # S: O(sum(L))
        # sum(L)为所有字符串的长度之和, S为 searchWord 的长度
        trie = Trie()
        for product in products:
            trie.insert(product)
        
        res = []
        prefix = ''
        for char in searchWord:
            prefix += char
            res.append(trie.search(prefix))
        return res
