class Solution:
    def check(self, arr):
        for e in arr:
            if e % 2 == 0:
                return False
        return True

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(0, len(arr) -2):
            if self.check(arr[i: i+3]):
                return True
        return False
