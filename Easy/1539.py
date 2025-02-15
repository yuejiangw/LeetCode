from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        '''
        缺失的数字可以用 arr[i] - (i + 1) 计算, 表示 arr[i] 前面缺失的数字个数
        使用 binary search 找到某个位置 i，使得 arr[i] - (i + 1) < k 但 arr[i + 1] - (i + 2) >= k
        说明第 k 个缺失的数就在 arr[i] 之后
        T: O(logn), S: O(1)
        '''
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m] - (m + 1) >= k:
                r = m - 1
            else:
                l = m + 1
        
        # 结果为 arr[l - 1] + (k - missing(arr[l - 1]))
        # missing(arr[l - 1]) = arr[l - 1] - (l - 1 + 1) = arr[l - 1] - l
        # 打开括号后可得结果为 l + k
        return l + k


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i, j = 0, 1
        while i < len(arr) and k > 0:
            if j == arr[i]:
                j += 1
                i += 1
            else:
                j += 1
                k -= 1
        return j - 1 if k == 0 else j + k - 1