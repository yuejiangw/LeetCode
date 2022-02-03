from collections import defaultdict


class Leaderboard:

    def __init__(self):
        self.board = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.board[playerId] += score

    def top(self, K: int) -> int:
        scores = sorted(self.board.values(), reverse=True)
        return sum(scores[:K])

    def reset(self, playerId: int) -> None:
        self.board[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
