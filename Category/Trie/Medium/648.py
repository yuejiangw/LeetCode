from typing import List

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
    
    def get_successor(self, word: str) -> str:
        curr = self.root
        successor = ''
        i = 0
        while curr and i < len(word) and word[i] in curr.children:
            curr = curr.children[word[i]]
            successor += word[i]
            i += 1
            if curr.is_word:
                return successor
        return ''


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for successor in dictionary:
            trie.insert(successor)
        
        res = ''
        for s in sentence.split(' '):
            successor = trie.get_successor(s)
            if successor == '':
                res += s
            else:
                res += successor
            res += ' '
        return res.strip()
