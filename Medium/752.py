from typing import List
from collections import deque


class Solution:
    def plus_one(self, s, j):
        s = list(s)
        if s[j] == '9':
            s[j] = '0'
        else:
            s[j] = str(int(s[j]) + 1)
        return ''.join(s)

    def minus_one(self, s, j):
        s = list(s)
        if s[j] == '0':
            s[j] = '9'
        else:
            s[j] = str(int(s[j]) - 1)
        return ''.join(s)

    def openLock(self, deadends: List[str], target: str) -> int:
        """ Find a shortest path from a graph, use BFS. """
        deadends = set(deadends)
        visited = set()
        queue = deque(['0000'])
        visited.add('0000')
        step = 0

        while queue:
            length = len(queue)
            for _ in range(length):
                curr = queue.popleft()
                if curr in deadends:
                    continue
                if curr == target:
                    return step
                for j in range(4):
                    up = self.plus_one(curr, j)
                    if up not in visited:
                        queue.append(up)
                        visited.add(up)
                    down = self.minus_one(curr, j)
                    if down not in visited:
                        queue.append(down)
                        visited.add(down)
            step += 1

        return -1
