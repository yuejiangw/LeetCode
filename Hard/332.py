from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjacent = defaultdict(list)
        for ticket in tickets:
            adjacent[ticket[0]].append(ticket[1])
        path = ['JFK']

        def backtracking(start):
            if len(path) == len(tickets) + 1:
                return True
            adjacent[start].sort()
            for _ in adjacent[start]:
                end_point = adjacent[start].pop(0)
                path.append(end_point)
                if backtracking(end_point):
                    return True
                path.pop()
                adjacent[start].append(end_point)
            return False

        backtracking('JFK')
        return path
