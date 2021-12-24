class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.symbol = {1: 'X', 2: 'O'}
        self.board = [['' for _ in range(n)] for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        def get_col(col):
            return [self.board[i][col] for i in range(self.n)]

        def get_catercorner(row, col):
            catercorner_1 = [self.board[i][i] for i in range(self.n)]
            catercorner_2 = [self.board[i][self.n-1-i] for i in range(self.n)]
            if row == col and row + col == self.n - 1:
                return catercorner_1, catercorner_2
            elif row == col:
                return catercorner_1
            elif row + col == self.n - 1:
                return catercorner_2

        sbl = self.symbol[player]
        win_list = [sbl for _ in range(self.n)]
        self.board[row][col] = sbl
        if self.board[row] == win_list:
            return player
        if get_col(col) == win_list:
            return player
        if col == row or col + row == self.n - 1:
            if col == row and col + row == self.n - 1:
                c1, c2 = get_catercorner(row, col)
                if c1 == win_list or c2 == win_list:
                    return player
            else:
                c = get_catercorner(row, col)
                if c == win_list:
                    return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
