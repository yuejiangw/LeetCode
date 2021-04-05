class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        candidates = []
        for word in dictionary:
            tmp = list(s[::])
            i = 0
            j = 0
            while i < len(tmp):
                if j < len(word) and tmp[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    del tmp[i]
            if ''.join(tmp) == word:
                candidates.append(word)
        
        if candidates:
            target = candidates[0]
            for i in range(1, len(candidates)):
                if len(candidates[i]) > len(target):
                    target = candidates[i]
                # 返回字典序较小的word
                if len(candidates[i]) == len(target) and candidates[i] < target:
                    target = candidates[i]
            return target
        else:
            return ''