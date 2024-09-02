import heapq
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # T: O(logn + k)
        # S: O(1)

        def left_bound(nums, target):
            i, j = 0, len(nums)
            while i < j:
                mid = i + (j - i) // 2
                if nums[mid] >= target:
                    j = mid
                else:
                    i = mid + 1
            return i
        
        # 找到 x 的左边界
        p = left_bound(arr, x)
        # 两端都开区间 (left, right)
        left, right = p - 1, p
        # 中心扩散，直到区间内包含 k 个元素
        while right - left - 1 < k:
            if left == -1:
                right += 1
            elif right == len(arr):
                left -= 1
            elif x - arr[left] > arr[right] - x:
                right += 1
            else:
                left -= 1
        return arr[left + 1: right]

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """ 小顶堆 """
        heap = []
        for num in arr:
            # heappush 接受两个参数，第一个是 heap，第二个是 element
            # 当 element 为元组时，会以 element[0] 作为 key 进行排序
            # 由题意得，key 应该为 (abs(num - x), num)，代表默认情况
            # 下以绝对值之差作为比较器，有冲突时按照 num 的大小进行排序
            heapq.heappush(heap, ((abs(num - x), num), num))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return sorted(res)

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """ 排序 """
        arr = sorted(arr, key=lambda n: (abs(n - x), n))
        return sorted(arr[:k])
