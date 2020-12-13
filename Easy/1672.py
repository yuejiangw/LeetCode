class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        results = []
        for i in range(len(accounts)):
            result = 0
            for j in range(len(accounts[i])):
                result += accounts[i][j]
            results.append(result)
        return max(results)