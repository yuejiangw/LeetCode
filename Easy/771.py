class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        result = 0
        for character in S:
            if character in J:
                result += 1
        return result