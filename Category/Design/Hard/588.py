from typing import List


class Node:
    def __init__(self, name, is_file=False):
        self.name = name
        self.children = {}
        self.content = ''
        self.is_file = is_file

class FileSystem:

    def __init__(self):
        self.root = Node('/')

    def find_node(self, path:str) -> Node:
        curr = self.root
        if path == '/':
            return curr
        path = path.split('/')
        # 跳过第一个路径因为是 ''
        i = 1
        while curr and i < len(path):
            p = path[i]
            # 如果路径存在则进入该路径，否则创建该路径
            if p not in curr.children:
                curr.children[p] = Node(p)
            curr = curr.children[p]
            i += 1
        return curr

    def ls(self, path: str) -> List[str]:
        node = self.find_node(path)
        if node.is_file:
            return [node.name]
        res = []
        for k in node.children.keys():
            res.append(k)
        return sorted(res)

    def mkdir(self, path: str) -> None:
        self.find_node(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.find_node(filePath)
        node.is_file = True
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self.find_node(filePath)
        return node.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)