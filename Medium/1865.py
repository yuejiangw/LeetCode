from collections import Counter
from typing import List


class FindSumPairs:
    """ 注意题干中条件，nums1的最大长度小于nums2，所以固定nums2遍历nums1会比较快 """

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counts = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        # decrease the count of original val by 1.
        old = self.nums2[index]
        self.counts[old] -= 1
        # add val to nums2[index], then update the count table.
        self.nums2[index] += val
        new = self.nums2[index]
        if new not in self.counts:
            self.counts[new] = 0
        self.counts[new] += 1

    def count(self, tot: int) -> int:
        res = 0
        for num in self.nums1:
            res += self.counts.get(tot - num, 0)
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
