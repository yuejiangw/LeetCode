class Solution:
    def minCount(self, coins: List[int]) -> int:
        result = 0
        for coin in coins:
            if coin % 2 == 0:
                result += int(coin / 2)
            else:
                result += int(coin / 2) + 1
        return result