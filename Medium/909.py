from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # T: O(n^2)
        # S: O(n^2)
        n = len(board)
        arr = [0] * (n * n + 1)
        is_right = True
        
        idx = 1
        for i in range(n - 1, -1, -1):
            if is_right:
                for j in range(n):
                    arr[idx] = board[i][j]
                    idx += 1
            else:
                for j in range(n - 1, -1, -1):
                    arr[idx] = board[i][j]
                    idx += 1
            is_right = not is_right
        
        queue = deque([1])
        visited = set([1])
        res = 0

        while queue:
            length = len(queue)
            for _ in range(length):
                curr = queue.popleft()
                if curr == n * n:
                    return res
                for i in range(curr + 1, min(curr + 6, n * n) + 1):
                    # 关键: 要先获取 next 再判断 visited
                    # 因为遇到梯子节点我们会直接访问梯子节点, 而不是它的前置节点
                    nxt = i
                    if arr[nxt] != -1:
                        nxt = arr[nxt]
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
            res += 1
        return -1
