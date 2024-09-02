import heapq
from typing import List

class State:
    def __init__(self, id: int, costFromSrc: int, nodeNumFromSrc: int) -> None:
        self.id = id
        self.costFromSrc = costFromSrc
        self.nodeNumFromSrc = nodeNumFromSrc
    
    def __lt__(self, other) -> bool:
        return self.costFromSrc < other.costFromSrc

def dijkstra(graph, src, k, dst):
    # 从 src 到节点 i 的最短路径权重为 distTo[i]
    distTo = [float('inf') for _ in range(len(graph))]
    # 从 src 到节点 i 的最小权重路径至少要经过 nodeNumTo[i] 个节点
    nodeNumTo = [float('inf') for _ in range(len(graph))]
    # base case
    distTo[src], nodeNumTo[src] = 0, 0

    # 优先队列
    pq = []
    # BFS
    heapq.heappush(pq, State(src, 0, 0))
    while pq:
        currState = heapq.heappop(pq)
        currId = currState.id
        currCostFromSrc = currState.costFromSrc
        currNodeNumFromSrc = currState.nodeNumFromSrc

        if currId == dst:
            # 找到最短路径
            return currCostFromSrc
        if currNodeNumFromSrc == k:
            # 中转次数耗尽
            continue
        
        for neighbor in graph[currId]:
            nextId = neighbor[0]
            costToNextCity = neighbor[1] + currCostFromSrc
            # 中转次数消耗 1
            nextNodeNumFromSrc = currNodeNumFromSrc + 1 
            if distTo[nextId] > costToNextCity:
                distTo[nextId] = costToNextCity
                nodeNumTo[nextId] = nextNodeNumFromSrc
            # 剪枝，如果中转次数更多花费还更大，那必然不是最短路径
            if costToNextCity > distTo[nextId] and nextNodeNumFromSrc > nodeNumTo[nextId]:
                continue
            
            heapq.heappush(pq, State(nextId, costToNextCity, nextNodeNumFromSrc))
    return -1


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for start, end, price in flights:
            graph[start].append([end, price])
        
        # 最多有 k 个中转城市，算上最后的 dst 一共可以走 k + 1 步
        k += 1
        return dijkstra(graph, src, k, dst)