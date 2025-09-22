class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # 建图
        graph_red = defaultdict(list)
        graph_blue = defaultdict(list)
        for x, y in redEdges:
            graph_red[x].append(y)
        for x, y in blueEdges:
            graph_blue[x].append(y)

        RED = 0
        BLUE = 1
        # dist[i] = [0 to i dist start with RED, 0 to i dist start with BLUE]
        dist = [[float('inf')] * 2 for _ in range(n)]
        dist[0][RED] = dist[0][BLUE] = 0
        queue = deque([(0, RED), (0, BLUE)])
        while queue:
            u, c = queue.popleft()
            next_color = BLUE if c == RED else RED
            next_graph = graph_blue if c == RED else graph_red
            for adj in next_graph[u]:
                if dist[adj][next_color] == float('inf'):
                    dist[adj][next_color] = dist[u][c] + 1
                    queue.append((adj, next_color))
        res = []
        for i in range(n):
            d = min(dist[i])
            res.append(-1 if d == float('inf') else d)
        return res
