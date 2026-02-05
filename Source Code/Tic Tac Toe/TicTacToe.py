"""
File: TicTacToe.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements a console-based Tic Tac Toe game for two players. 
    It demonstrates game theory concepts, state management, and win condition 
    detection using a service-based architecture.

Complexity Analysis:
    - Time Complexity: O(1) per move (constant board size).
    - Space Complexity: O(1) for the 3x3 board.

Logic:
    1. Initialize a 3x3 game board.
    2. Alternate turns between Player 1 (X) and Player 2 (O).
    3. Validate moves to prevent overwriting occupied cells.
    4. Check win conditions after each move (rows, columns, diagonals).
    5. Detect draw when all cells are filled with no winner.
"""

from typing import List, Optional, Tuple


class TicTacToeService:
    """
    A service class for managing Tic Tac Toe game state and logic.
    """

    PLAYER_X = 'X'
    PLAYER_O = 'O'
    EMPTY = ' '

    def __init__(self):
        """Initializes a new game."""
        self.board: List[str] = [self.EMPTY] * 9
        self.current_player: str = self.PLAYER_X
        self.winner: Optional[str] = None
        self.game_over: bool = False
        self.moves_count: int = 0

    def reset(self) -> None:
        """Resets the game to initial state."""
        self.board = [self.EMPTY] * 9
        self.current_player = self.PLAYER_X
        self.winner = None
        self.game_over = False
        self.moves_count = 0

    def make_move(self, position: int) -> Tuple[bool, str]:
        """
        Makes a move at the specified position.
        
        Args:
            position: Board position (0-8).
            
        Returns:
            Tuple of (success, message).
        """
        if self.game_over:
            return False, "Game is over!"

        if position < 0 or position > 8:
            return False, "Invalid position! Use 0-8."

        if self.board[position] != self.EMPTY:
            return False, "Cell already occupied!"

        self.board[position] = self.current_player
        self.moves_count += 1

        if self._check_winner():
            self.winner = self.current_player
            self.game_over = True
            return True, f"Player {self.current_player} wins!"

        if self.moves_count >= 9:
            self.game_over = True
            return True, "Game drawn!"

        self.current_player = self.PLAYER_O if self.current_player == self.PLAYER_X else self.PLAYER_X
        return True, f"Player {self.current_player}'s turn"

    def _check_winner(self) -> bool:
        """Checks if the current player has won."""
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]

        for pattern in win_patterns:
            if (self.board[pattern[0]] == self.board[pattern[1]] == 
                self.board[pattern[2]] == self.current_player):
                return True
        return False

    def get_board_display(self) -> str:
        """Returns a formatted string representation of the board."""
        lines = [
            "=============",
            f"| {self._cell(0)} | {self._cell(1)} | {self._cell(2)} |",
            "=============",
            f"| {self._cell(3)} | {self._cell(4)} | {self._cell(5)} |",
            "=============",
            f"| {self._cell(6)} | {self._cell(7)} | {self._cell(8)} |",
            "============="
        ]
        return '\n'.join(lines)

    def _cell(self, pos: int) -> str:
        """Returns cell display value (position number if empty)."""
        return self.board[pos] if self.board[pos] != self.EMPTY else str(pos)


def main():
    """
    Demonstrates the Tic Tac Toe game with a sample playthrough.
    """
    print("--- Tic Tac Toe Service Demo ---\n")
    
    game = TicTacToeService()
    
    # Sample game playthrough
    moves = [4, 0, 2, 6, 1, 3, 7]  # X wins with middle row
    
    print("Initial Board:")
    print(game.get_board_display())
    
    for move in moves:
        print(f"\nPlayer {game.current_player} plays position {move}")
        success, message = game.make_move(move)
        print(game.get_board_display())
        print(f"Result: {message}")
        
        if game.game_over:
            break
    
    print("\n--- Game Complete ---")
    if game.winner:
        print(f"Winner: Player {game.winner}")
    else:
        print("Result: Draw")


if __name__ == "__main__":
    main()
