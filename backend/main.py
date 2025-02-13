from fastapi import FastAPI
from pydantic import BaseModel
from game_logic.tic_tac_toe import TicTacToe
from game_logic.ai import TicTacToeAI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow frontend requests
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

game = TicTacToe()  # Create a new game instance
ai = TicTacToeAI(game)


class Move(BaseModel):
    row: int
    col: int
    player: int  # 1 for human, -1 for AI


@app.get("/")
def read_root():
    """Root endpoint to check if the API is running"""
    return {"message": "Tic-Tac-Toe API is running!"}


@app.post("/move/")
def make_move(move: Move):
    """Endpoint to make a move"""
    if game.make_move(move.row, move.col, move.player):
        winner = game.check_winner()
        return {"board": game.board.tolist(), "winner": winner}
    return {"error": "Invalid move. Try again!"}


@app.get("/reset/")
def reset_game():
    """Endpoint to reset the game"""
    game.reset_board()
    return {"message": "Game reset!", "board": game.board.tolist()}


@app.get("/state/")
def get_state():
    """Endpoint to get the current game state"""
    return {
        "board": game.board.tolist(),  # Convert NumPy array to a Python list
        # Ensure winner is a Python int
        "winner": int(game.winner) if game.winner is not None else None
    }


@app.get("/ai-move/")
def ai_move():
    """Endpoint to get AI's best move"""
    move = ai.best_move()

    if move:
        game.make_move(move[0], move[1], -1)  # AI makes the move
        winner = game.check_winner()

        return {
            "board": game.board.tolist(),  # Convert NumPy array to a Python list
            # Convert NumPy int to Python int
            "winner": int(winner) if winner is not None else None
        }

    return {"error": "No valid moves left!"}
