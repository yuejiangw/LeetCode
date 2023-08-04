from typing import List


class Node:
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.is_word = True

    def search(self, word: str) -> bool:
        def dfs(curr: Node, diff_num: int, idx: int) -> bool:
            if not curr or diff_num > 1:
                return False
            # 遍历到 word 末尾的时候要判断是否搜索到了一个有效的单词，并且 diff_num 恰好为 1
            if idx == len(word):
                return curr.is_word and diff_num == 1

            # 由于可能同时插入与 word 相同的单词以及与 word 仅相差 1 个字母的单词，
            # 因此每次 dfs 我们都要判断每一个 child 的值
            for k, v in curr.children.items():
                if k == word[idx]:
                    if dfs(curr.children[word[idx]], diff_num, idx + 1):
                        return True
                else:
                    if diff_num == 0 and dfs(v, diff_num + 1, idx + 1):
                        return True
            return False

        return dfs(self.root, 0, 0)


class MagicDictionary:
    def __init__(self):
        self.dictionary = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.dictionary.insert(word)

    def search(self, searchWord: str) -> bool:
        return self.dictionary.search(searchWord)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
