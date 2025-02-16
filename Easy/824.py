class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        # T: O(n), S: O(n)
        res = []
        vowel = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        sentence = sentence.split()
        for idx, word in enumerate(sentence):
            if word[0] in vowel:
                word += 'ma'
            else:
                word = word[1:] + word[0] + 'ma'
            word += 'a' * (idx + 1)
            res.append(word)
        return ' '.join(res)
