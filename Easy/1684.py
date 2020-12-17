class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            flag = True
            for character in word:
                if allowed.find(character) == -1:
                    flag = False
                    break
            if flag:
                count += 1
        return count