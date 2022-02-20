from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        贪心, 由于每艘船最多坐两个人, 因此先排序之后用双指针分别讨论最大体重和最小体重的人
        如果两人可以同坐一艘船则同时移动两个指针, 否则单独减少右端指针
        时间复杂度: 排序 O(NlogN)
        空间复杂度: 排序一般都是快速排序, 要用到递归, 深度为 logN, 所以为 O(logN)
        """
        people.sort()
        res = 0
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] > limit:
                j -= 1
            else:
                i += 1
                j -= 1
            res += 1
        return res