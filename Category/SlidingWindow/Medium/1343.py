class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = r = 0
        window = res = 0
        while r < len(arr):
            # expand
            c = arr[r]
            r += 1
            window += c
            if r - l < k:
                continue
            # collect
            if window / k >= threshold:
                res += 1
            # shrink
            d = arr[l]
            l += 1
            window -= d
        return res