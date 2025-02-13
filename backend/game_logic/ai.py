import numpy as np
from game_logic.tic_tac_toe import TicTacToe


class TicTacToeAI:
    def __init__(self, game: TicTacToe):
        self.game = game  # Link to the game instance

    def minimax(self, board, depth, is_maximizing):
        """Minimax algorithm to find the best move"""
        winner = self.game.check_winner()

        # Base case: Check for a winner or draw
        if winner == 1:   # Human wins
            return -10 + depth
        elif winner == -1:  # AI wins
            return 10 - depth
        elif self.game.is_full():  # Draw
            return 0

        if is_maximizing:  # AI's turn (maximize score)
            best_score = -float("inf")
            for row in range(3):
                for col in range(3):
                    if board[row, col] == 0:  # Check empty spots
                        board[row, col] = -1  # AI move
                        score = self.minimax(board, depth + 1, False)
                        board[row, col] = 0  # Undo move
                        best_score = max(score, best_score)
            return best_score
        else:  # Human's turn (minimize AI score)
            best_score = float("inf")
            for row in range(3):
                for col in range(3):
                    if board[row, col] == 0:
                        board[row, col] = 1  # Human move
                        score = self.minimax(board, depth + 1, True)
                        board[row, col] = 0  # Undo move
                        best_score = min(score, best_score)
            return best_score

    def best_move(self):
        """Find the best move for AI"""
        best_score = -float("inf")
        move = None
        for row in range(3):
            for col in range(3):
                if self.game.board[row, col] == 0:  # Check empty spots
                    self.game.board[row, col] = -1  # AI move
                    score = self.minimax(self.game.board, 0, False)
                    self.game.board[row, col] = 0  # Undo move
                    if score > best_score:
                        best_score = score
                        move = (row, col)
        return move  # Returns (row, col) tuple
