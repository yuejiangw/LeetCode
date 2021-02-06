# 解题思路：无论k有多大，胜利者都在arr数组中，尝试一次遍历。
# 遇见arr数组中的最大值之前都没有满足条件的胜利者，那么胜利者一定是这个最大值。
# 最多遍历一次就会遇见arr数组中的最大值，所以输掉的就不用再考虑
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner, count = arr[0], 0
        i = 1
        for i in range(1, len(arr)):
            if (arr[i] < winner):
                count += 1
            else:
                winner = arr[i]
                count = 1
            if count == k:
                break
        return winner