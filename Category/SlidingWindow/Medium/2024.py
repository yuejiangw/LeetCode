class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def traverse(answerKey, k, answer_to_change: str):
            l = r = 0
            expected_answer = 'T' if answer_to_change == 'F' else 'F'
            res = 0
            while r < len(answerKey):
                c = answerKey[r]
                r += 1
                if c == answer_to_change:
                    k -= 1
                while l < r and k < 0:
                    d = answerKey[l]
                    l += 1
                    if d == answer_to_change:
                        k += 1
                res = max(res, r - l)
            return res
        
        return max(traverse(answerKey, k, 'T'), traverse(answerKey, k, 'F'))
