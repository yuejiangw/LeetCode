class Solution:
    def search(self, L: int, n: int, S: str) -> str:
        """
        Search a substring of given length
        that occurs at least 2 times.
        @return start position if the substring exits and -1 otherwise.
        """
        # 这里的 L 是子串的长度
        seen = set()
        for start in range(0, n - L + 1):
            tmp = S[start:start + L]
            # 为了减少空间，我们不直接存储子串，而是存储子串的 hash 值
            h = hash(tmp)
            # 只要重复出现，即可返回，无需考虑次数
            if h in seen:
                return start
            seen.add(h)
        return -1
        
    def longestRepeatingSubstring(self, S: str) -> str:
        # 如果长度为 k 的子串是重复子串，则长度为 k-1、k-2、... 1 的子串也是重复子串
        # 我们可以通过二分查找确定这个最大的 k
        # T: O(NlogN)
        # S: O(N)
        n = len(S)
        
        # binary search, L = repeating string length
        left, right = 1, n
        while left <= right:
            L = left + (right - left) // 2
            # search 方法用来在 S 中 搜索是否有相同的子串出现
            if self.search(L, n, S) != -1:
                left = L + 1
            else:
                right = L - 1
               
        return left - 1
