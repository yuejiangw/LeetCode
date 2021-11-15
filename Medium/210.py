from typing import List

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
