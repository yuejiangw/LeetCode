from collections import defaultdict


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        '''
        找一个长度为k的子数组，要求B的数量最大 - 定长滑动窗口
        '''
        l = r = 0
        window = 0
        res = float('inf')
        while r < len(blocks):
            # expand
            c = blocks[r]
            r += 1    
            window += 1 if c == 'W' else 0
            # skip invalid window size
            if r - l < k:
                continue
            # collect
            res = min(res, window)
            # shrink
            d = blocks[l]
            l += 1
            window -= 1 if d == 'W' else 0
        return res
            
