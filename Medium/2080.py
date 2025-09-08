from typing import List
from collections import defaultdict
from bisect import bisect_left, bisect_right

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.val_to_idx = defaultdict(list)
        for i, n in enumerate(arr):
            self.val_to_idx[n].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        # 33: [1, 7] -> [0, 11]
        indices = self.val_to_idx[value]
        start, end = bisect_left(indices, left), bisect_right(indices, right)
        return end - start 



# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)