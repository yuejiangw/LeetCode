from typing import List
from collections import defaultdict

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """思路
        贪心，只需要检查是否翻转 tops[0] 还是 bottoms[0] 即可
        """
        # T: O(N)
        # S: O(1)
        N = len(tops)

        def check(x):
            top_rotate = 0
            bottom_rotate = 0
            for i in range(N):
                if tops[i] != x and bottoms[i] != x:
                    return -1
                elif tops[i] != x:
                    top_rotate += 1
                elif bottoms[i] != x:
                    bottom_rotate += 1
            return min(top_rotate, bottom_rotate)
        
        res = check(tops[0])
        if res != -1 or tops[0] == bottoms[0]:
            return res
        return check(bottoms[0])


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # T: O(N)
        # S: O(N)
        N = len(tops)
        all_pos = set(range(N))
        res = float('inf')

        top_pos = defaultdict(set)
        bottom_pos = defaultdict(set)
        for i, n in enumerate(tops):
            top_pos[n].add(i)
        for i, n in enumerate(bottoms):
            bottom_pos[n].add(i)
        
        for num, pos in top_pos.items():
            if pos.union(bottom_pos[num]) == all_pos:
                res = min(res, N - max(len(pos), len(bottom_pos[num])))
        return res if res != float('inf') else -1
