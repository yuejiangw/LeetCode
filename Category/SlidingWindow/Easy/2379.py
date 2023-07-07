from collections import defaultdict


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """
        翻译题目，在 blocks 数组内找到一个长度为 k 子数组，要求它含有最少的白色块，返回这个白色块的数量
        """
        l, r = 0, 0
        window = defaultdict(int)
        window_size = 0
        res = float("inf")
        while r < len(blocks):
            # 窗口扩张
            c = blocks[r]
            r += 1
            window[c] += 1
            window_size += 1
            # 窗口收缩
            if window_size > k:
                d = blocks[l]
                l += 1
                window[d] -= 1
                window_size -= 1
            # 更新结果
            if window_size == k:
                res = min(res, window["W"])
        return res
