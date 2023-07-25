from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def get_score(player: List[int]) -> int:
            res = 0
            for i, score in enumerate(player):
                if i == 0:
                    res += score
                elif i == 1:
                    if player[i - 1] == 10:
                        res += score * 2
                    else:
                        res += score
                else:
                    if player[i - 1] == 10 or player[i - 2] == 10:
                        res += score * 2
                    else:
                        res += score
            return res

        score1 = get_score(player1)
        score2 = get_score(player2)
        if score1 == score2:
            return 0
        return 1 if score1 > score2 else 2
