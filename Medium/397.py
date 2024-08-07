from collections import deque


class Solution:
    def integerReplacement(self, n: int) -> int:
        '''
        BFS
        采用集合去重可以有效优化时间
        8 -> 4 -> 2 -> 1
        '''
        queue = deque([n])
        res = 0
        visited = set()
        while queue:
            l = len(queue)
            for _ in range(l):
                curr = queue.popleft()
                visited.add(curr)
                if curr == 1:
                    return res
                if curr % 2 == 0:
                    if curr // 2 not in visited:
                        queue.append(curr // 2)
                elif curr % 2 == 1:
                    if curr + 1 not in visited:
                        queue.append(curr + 1)
                    if curr - 1 not in visited:
                        queue.append(curr - 1)
            res += 1
        return res