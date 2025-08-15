from collections import defaultdict, deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        '''
        topological sorting + BFS
        假设共有 n 个单词，单词的平均长度是 m
        T: O(mn)
        S: O(mn)
        '''
        # 邻接表, graph[u] = {v1, v2, ...} 表示 u 在 v1, v2 之前
        graph = defaultdict(set)
        # 入度表
        indegree = defaultdict(int)
        for word in words:
            for c in word:
                indegree[c] = 0

        # build graph
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_length = min(len(word1), len(word2))

            # 检查是否出现非法情况
            if len(word1) > len(word2) and word1[:min_length] == word2[:min_length]:
                return ''
            
            # 找到第一个不同的字符，建立依赖关系
            for j in range(min_length):
                if word1[j] != word2[j]:    # word1[j] < word2[j]
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break   # 只需要第一个不同的字母

        queue = deque([char for char in indegree if indegree[char] == 0])
        res = []

        while queue:
            char = queue.popleft()
            res.append(char)
            for neighbor in graph[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # check for cycles
        if len(res) != len(indegree):
            return ''
        
        return ''.join(res)


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
        