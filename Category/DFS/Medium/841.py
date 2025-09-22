from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(start):
            visited.add(start)
            for adj in rooms[start]:
                if adj not in visited:
                    dfs(adj)
        
        dfs(0)
        return len(visited) == len(rooms)