"""
思路

贪心策略，袋子里只有三种物品，1，0，-1。想要让袋子里的物品和最大，那么就要尽可能多的放1，
然后放0，最后放-1。如果1的数量加上0的数量大于等于k，那么就可以放下k个物品，
否则就放下尽可能多的1，然后放下尽可能多的0，最后放下尽可能多的-1。
"""


class Solution:
    def kItemsWithMaximumSum(
        self, numOnes: int, numZeros: int, numNegOnes: int, k: int
    ) -> int:
        if numOnes + numZeros >= k:
            return min(numOnes, k)
        else:
            return numOnes - (k - numOnes - numZeros)
