class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[:n]
        y = nums[n:]
        results = []
        for i in range(len(x)):
            results.append(x[i])
            results.append(y[i])
        return results
