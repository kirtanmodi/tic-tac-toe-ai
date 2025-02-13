import numpy as np


class TicTacToe:
    def __init__(self):
        """Initialize an empty 3x3 board"""
        self.board = np.zeros(
            (3, 3), dtype=int)  # 0 = empty, 1 = player, -1 = AI
        self.winner = None  # Stores the winner (1 = player, -1 = AI, 0 = draw)

    def reset_board(self):
        """Resets the board to start a new game"""
        self.board.fill(0)
        self.winner = None

    def make_move(self, row, col, player):
        """
        Places a move on the board.
        :param row: Row index (0-2)
        :param col: Column index (0-2)
        :param player: 1 (human) or -1 (AI)
        :return: True if move is valid, False otherwise
        """
        if self.board[row, col] == 0:
            self.board[row, col] = player
            return True
        return False

    def check_winner(self):
        """
        Checks if the game has a winner or if it's a draw.
        Updates self.winner accordingly.
        """
        # Check rows, columns, and diagonals
        for i in range(3):
            if abs(sum(self.board[i, :])) == 3:  # Row win
                self.winner = np.sign(sum(self.board[i, :]))
                return self.winner
            if abs(sum(self.board[:, i])) == 3:  # Column win
                self.winner = np.sign(sum(self.board[:, i]))
                return self.winner

        # Check diagonals
        if abs(sum(self.board.diagonal())) == 3:
            self.winner = np.sign(sum(self.board.diagonal()))
            return self.winner
        if abs(sum(np.fliplr(self.board).diagonal())) == 3:
            self.winner = np.sign(sum(np.fliplr(self.board).diagonal()))
            return self.winner

        # Check for draw
        if not (self.board == 0).any():
            self.winner = 0  # Draw
            return 0

        return None  # No winner yet

    def is_full(self):
        """Checks if the board is full"""
        return not (self.board == 0).any()

    def display_board(self):
        """Prints the board (for debugging)"""
        symbols = {0: "-", 1: "X", -1: "O"}
        for row in self.board:
            print(" | ".join(symbols[cell] for cell in row))
        print("\n")


# Example Usage:
if __name__ == "__main__":
    game = TicTacToe()
    game.display_board()
    game.make_move(0, 0, 1)
    game.display_board()
    print("Winner:", game.check_winner())
