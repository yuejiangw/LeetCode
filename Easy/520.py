class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # 全大写
        if word.upper() == word:
            return True
        # 全小写
        if word.lower() == word:
            return True

        # 首字母小写
        if word[0].lower() == word[0]:
            return False
        # 首字母大写
        else:
            for i in range(1, len(word)):
                if word[i] >= 'A' and word[i] <= 'Z':
                    return False
            return True
