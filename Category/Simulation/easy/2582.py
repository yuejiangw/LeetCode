class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # T: O(1)
        # S: O(1)
        rounds = time // (n - 1)
        offset = time % (n - 1)
        return offset + 1 if rounds % 2 == 0 else n - offset
