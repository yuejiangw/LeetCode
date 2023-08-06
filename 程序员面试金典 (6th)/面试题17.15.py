from typing import List


class Node:
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.is_word = True

    def check(self, word):
        if word == "":
            return True
        curr = self.root
        for i, c in enumerate(word):
            if c not in curr.children:
                return False
            curr = curr.children[c]
            if curr.is_word and self.check(word[i + 1 :]):
                return True
        return False

        return dfs(word, 0)


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x: (len(x), x))
        trie = Trie()
        res = ""
        for word in words:
            if not word:
                continue
            if trie.check(word):
                if len(word) > len(res):
                    res = word
            else:
                trie.insert(word)
        return res
