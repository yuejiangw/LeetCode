from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        取第 k 大用小顶堆, 当堆中元素不足 k 个时候正常入堆调整, 否则就保持堆中元素始终为 k 个
        当前元素如果大于堆顶元素的时候就将堆顶元素弹出, 把当前元素入堆

        时间复杂度: O(Nlogk)
        空间复杂度: O(k)
        """
        heap = []
        i = 0
        while i < k:
            heapq.heappush(heap, nums[i])
            i += 1
        while i < len(nums):
            if nums[i] > heap[0]:
                heapq.heapreplace(heap, nums[i])
            i += 1
        return heap[0]
    
class Solution:
    '''
    quick select, 时间复杂度 O(n)
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right):
            pivot_idx = random.randint(left, right)
            nums[right], nums[pivot_idx] = nums[pivot_idx], nums[right]
            pivot = nums[right]
            store_idx = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_idx], nums[i] = nums[i], nums[store_idx]
                    store_idx += 1
            nums[store_idx], nums[right] = nums[right], nums[store_idx]
            return store_idx
        
        l, r = 0, len(nums) - 1
        target = len(nums) - k
        while True:
            p = partition(l, r)
            if p == target:
                return nums[p]
            elif p < target:
                l = p + 1
            else:
                r = p - 1
            