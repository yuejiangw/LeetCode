class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # 返回入度为0的节点集合即可
        end_set = set([y for x, y in edges])
        return [i for i in range(n) if i not in end_set]