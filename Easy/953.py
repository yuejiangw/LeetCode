from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pos = {c: i for i, c in enumerate(order)}
        return words == sorted(words, key=lambda w: [pos[x] for x in w])
