class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        '''
        当遍历到第i个位置时，如果可以切分为块，那前i个位置的最大值一定等于i。
        否则，一定有比i小的数划分到后面的块，那块排序后，一定不满足升序。
        '''
        if arr == None:
            return 0
        result = 0
        curr = arr[0]
        for i in range(len(arr)):
            curr = max(curr, arr[i])
            if curr == i:
                result += 1
        return result