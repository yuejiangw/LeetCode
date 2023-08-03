from typing import List


class Node:
    def __init__(self):
        self.fid = -1
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, dir: str, fid: int) -> None:
        dir = dir.split("/")
        curr = self.root
        for d in dir[1:]:
            if d not in curr.children:
                curr.children[d] = Node()
            curr = curr.children[d]
        curr.fid = fid

    def search(self) -> List[int]:
        res = []

        # 从根节点出发，任意一条路径只要找到一个 fid != -1 的节点就无需继续向下寻找了直接返回
        # 如果 fid == -1 说明还没遇到有效的路径，则我们对于当前节点的所有子节点继续 dfs
        def dfs(curr: Node):
            if curr.fid != -1:
                res.append(curr.fid)
                return
            for v in curr.children.values():
                dfs(v)

        dfs(self.root)
        return res


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for i, f in enumerate(folder):
            trie.insert(f, i)
        res = trie.search()
        return [folder[i] for i in res]
