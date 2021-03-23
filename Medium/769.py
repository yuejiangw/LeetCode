class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        if arr == None:
            return 0
        result = 0
        curr = arr[0]
        for i in range(len(arr)):
            curr = max(curr, arr[i])
            if curr == i:
                result += 1
        return result