class Connect4:
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 13)

    def is_valid_move(self, column):
        if column < 0 or column >= 7:
            return False
        return self.board[0][column] == ' '

    def make_move(self, column):
        if not self.is_valid_move(column):
            print("Invalid move. Try again.")
            return False

        for row in range(5, -1, -1):
            if self.board[row][column] == ' ':
                self.board[row][column] = self.current_player
                return True

    def check_winner(self):
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]  # Right, Down, Diagonal Right-Down, Diagonal Left-Down

        for row in range(6):
            for col in range(7):
                if self.board[row][col] != ' ':
                    for dr, dc in directions:
                        for i in range(1, 4):
                            r, c = row + i * dr, col + i * dc
                            if (
                                0 <= r < 6 and 0 <= c < 7 and
                                self.board[r][c] == self.board[row][col]
                            ):
                                if i == 3:
                                    return self.current_player
                            else:
                                break

        return None

    def is_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        while True:
            self.print_board()
            column = int(input(f"Player {self.current_player}, choose a column (0-6): "))
            if self.make_move(column):
                winner = self.check_winner()
                if winner:
                    self.print_board()
                    print(f"Player {winner} wins!")
                    break
                elif self.is_full():
                    self.print_board()
                    print("It's a tie!")
                    break
                self.switch_player()

# (b) Simple text-based version of the game
if __name__ == "__main__":
    game = Connect4()
    game.play()
