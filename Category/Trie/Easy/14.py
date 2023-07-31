from typing import List

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
    
    def get_longest_prefix(self) -> str:
        curr = self.root
        res = ''
        # 循环继续的条件有三个：节点存在、节点不是叶子、节点的孩子只有一个
        while curr and not curr.is_word and len(curr.children) == 1:
            # 从单元素字典中获取 key 和 value
            (key, value), = curr.children.items()
            res += key
            curr = value
        return res

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for s in strs:
            trie.insert(s)
        return trie.get_longest_prefix()


# 2022-02-13 前缀树解法
class Node:
    def __init__(self):
        self.children = [None] * 26
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = Node()
            curr = curr.children[idx]
        curr.is_word = True


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for s in strs:
            trie.insert(s)
        curr = trie.root
        level = 0
        continue_search = True
        while continue_search and curr and not curr.is_word:
            next_entry = None
            for child in curr.children:
                if child:
                    if not next_entry:
                        next_entry = child
                    else:
                        continue_search = False
            if continue_search:
                level += 1
                curr = next_entry
        return strs[0][:level]

# 2021-01-07
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 利用python的max()和min()，在Python里字符串是可以比较的，
        # 按照ascII值排，举例abb， aba，abac，最大为abb，最小为aba。
        # 所以只需要比较最大最小的公共前缀就是整个数组的公共前缀
        if not strs:
            return ""
        s1 = min(strs)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1
        
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """ 纯暴力 """
        min_len = len(min(strs, key=len))
        i = 0
        continue_find = True
        res = ''
        while continue_find and i < min_len:
            curr = None
            for s in strs:
                if curr:
                    if s[i] != curr:
                        continue_find = False
                        break
                curr = s[i]
            if continue_find:
                res += curr
                i += 1
        return res