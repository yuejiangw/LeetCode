class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        assert len(guess) == len(answer)
        result = 0
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                result += 1
        return result