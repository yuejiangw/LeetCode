class Solution:
    def dfs(self, isConnected, visited, i):
        for j in range(0, len(isConnected)):
            if isConnected[i][j] == 1 and not visited[j]:
                visited[j] = True
                self.dfs(isConnected, visited, j)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        counter = 0
        visited = [False] * len(isConnected)
        for i in range(len(isConnected)):
            if not visited[i]:
                self.dfs(isConnected, visited, i)
                counter += 1
        return counter
