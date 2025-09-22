from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 0:
            return list(range(numCourses))

        # 拓扑排序，根据所有节点的入度和出度给图定一个顺序
        # k:[[in], [out]]
        topo_dict = {k: [[], []] for k in range(numCourses)}
        for requist in prerequisites:
            in_node = requist[0]
            out_node = requist[1]
            topo_dict[in_node][0].append(out_node)
            topo_dict[out_node][1].append(in_node)

        def find_0_in(topo_dict):
            for k, v in topo_dict.items():
                if v[0] == []:
                    return k
            return -1

        res = []
        while topo_dict:
            k = find_0_in(topo_dict)
            if k == -1:
                return []
            else:
                res.append(k)
                for node in topo_dict[k][1]:
                    topo_dict[node][0].remove(k)
                del topo_dict[k]
        return res


class Solution:
    # BFS版本
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)] # 邻接表
        indegree = [0] * numCourses # 入度
        for b, a in prerequisites:
            graph[a].append(b)
            indegree[b] += 1
        
        # 根据入度初始化队列中的结点（入度为0）
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        count = 0
        res = []
        
        # BFS
        while queue:
            node = queue.popleft()
            count += 1
            res.append(node)
            for adj in graph[node]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    queue.append(adj)
        
        # 图中有环, 无法拓扑排序
        if count != numCourses:
            return []
        return res
    
class Solution:
    # 借助 map 的 BFS
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prerequisite_graph = defaultdict(set)
        dependent_graph = defaultdict(list)
        for a, b in prerequisites:
            prerequisite_graph[a].add(b)
            dependent_graph[b].append(a)
        
        queue = deque([])
        visited = [False] * numCourses
        for i in range(numCourses):
            # 没有先修课，可以作为起始节点
            if len(prerequisite_graph[i]) == 0:
                queue.append(i)
        
        res = []
        while queue:
            l = len(queue)
            for _ in range(l):
                course = queue.popleft()
                visited[course] = True
                res.append(course)
                for dependent in dependent_graph[course]:
                    prerequisite_graph[dependent].remove(course)
                    if len(prerequisite_graph[dependent]) == 0 and not visited[dependent]:
                        queue.append(dependent)
        
        return res if len(res) == numCourses else []
