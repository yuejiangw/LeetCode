class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l= 0
        h = len(letters) - 1
        while l <= h:
            m = l + (h - l) // 2
            if letters[m] <= target:
                l = m + 1
            else:
                h = m - 1
        return letters[l % len(letters)]
