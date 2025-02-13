import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

// const API_URL = "http://127.0.0.1:8000"; // Update if backend runs elsewhere
// const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";
const API_URL = process.env.REACT_APP_API_URL || "https://tic-tac-toe-ai-y17b.onrender.com";

const App = () => {
  const [board, setBoard] = useState([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
  ]);
  const [winner, setWinner] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchGameState();
  }, []);

  const fetchGameState = async () => {
    try {
      const response = await axios.get(`${API_URL}/state/`);
      setBoard(response.data.board);
      setWinner(response.data.winner);
    } catch (error) {
      console.error("Error fetching game state:", error);
    }
  };

  const handleMove = async (row, col) => {
    if (board[row][col] !== 0 || winner !== null) return;
    setLoading(true);

    try {
      // Player move
      await axios.post(`${API_URL}/move/`, { row, col, player: 1 });
      await fetchGameState();

      // If no winner, AI moves
      if (!winner) {
        try {
          const aiResponse = await axios.get(`${API_URL}/ai-move/`);
          if (aiResponse.data.error) {
            console.error("AI move error:", aiResponse.data.error);
            return;
          }

          const { board: newBoard, winner: newWinner } = aiResponse.data;
          setBoard(newBoard);
          setWinner(newWinner);
        } catch (error) {
          console.error("Error during AI move:", error.message);
          // Optionally show user-friendly error message
          alert("Something went wrong with the AI move. Please try again.");
        }
      }
    } catch (error) {
      console.error("Error making a move:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleReset = async () => {
    try {
      await axios.get(`${API_URL}/reset/`);
      fetchGameState();
      setWinner(null);
    } catch (error) {
      console.error("Error resetting game:", error);
    }
  };

  return (
    <div className="container">
      <h1>Tic-Tac-Toe AI</h1>
      <div className="board">
        {board.map((row, rowIndex) =>
          row.map((cell, colIndex) => (
            <button key={`${rowIndex}-${colIndex}`} className="cell" onClick={() => handleMove(rowIndex, colIndex)} disabled={loading || cell !== 0}>
              {cell === 1 ? "X" : cell === -1 ? "O" : ""}
            </button>
          ))
        )}
      </div>
      {winner !== null && <h2>{winner === 0 ? "It's a Draw!" : winner === 1 ? "You Win!" : "AI Wins!"}</h2>}
      <button className="reset" onClick={handleReset}>
        Reset Game
      </button>
    </div>
  );
};

export default App;
