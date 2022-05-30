from binhex import LINELEN
from collections import defaultdict, deque
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # 1. 构建字符集
        unknown_word = set()
        for word in words:
            unknown_word |= set(word)

        # 2. 构建有向图
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            max_len = max(len(w1), len(w2))
            for j in range(max_len):
                if j == len(w2):
                    return ''   # 不合法
                if j == len(w1):
                    break
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    indegree[w2[j]] += 1
                    break   # 只有第一个不同的字符可以确定顺序
        
        # 3. 拓扑排序
        queue = deque()
        visited = set()
        for word in unknown_word:
            if indegree[word] == 0:
                queue.append(word)
                visited.add(word)
        res = ''
        while queue:
            length = len(queue)
            for _ in range(length):
                w = queue.popleft()
                res += w
                for adj in graph[w]:
                    indegree[adj] -= 1
                    if adj not in visited and indegree[adj] == 0:
                        queue.append(adj)
                        visited.add(adj)
        return res if len(res) == len(unknown_word) else ''
        