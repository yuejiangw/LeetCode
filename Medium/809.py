from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def get_group(s):
            model = []
            cnt = []
            i = 0
            while i < len(s):
                j = i + 1
                while j < len(s) and s[j] == s[i]:
                    j += 1
                model.append(s[i])
                cnt.append(j - i)
                i = j
            return model, cnt
        
        s_model, s_cnt = get_group(s)
        res = 0
        for word in words:
            model, cnt = get_group(word)
            if model != s_model:
                continue
            is_expressive = True
            for i in range(len(cnt)):
                if cnt[i] == s_cnt[i]:
                    continue
                elif cnt[i] > s_cnt[i]:
                    is_expressive = False
                    break
                else:
                    if s_cnt[i] < 3:
                        is_expressive = False
                        break
            if is_expressive:
                res += 1
        return res




