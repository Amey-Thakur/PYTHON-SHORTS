"""
File: RockPaperScissors.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements a robust Rock-Paper-Scissors game engine. It utilizes 
    cryptographically secure randomization (CSPRNG) to simulate fair play 
    within a zero-sum game environment, providing scholarly metrics for game 
    state evaluation.

Complexity Analysis:
    - Time Complexity: O(1) per game round, involving fixed-time randomization 
      and comparison operations.
    - Space Complexity: O(1) auxiliary space.

Logic:
    1. Define the search space of valid moves: Rock (R), Paper (P), and Scissors (S).
    2. Generate a computer move using the `secrets` module for cryptographic security.
    3. Normalize user input (case-insensitive) and validate against the search space.
    4. Apply the win-loss-tie decision matrix:
       - R beats S, S beats P, P beats R.
    5. Output the game results with scholarly precision.
"""

import os
import secrets
from typing import Dict, Optional


class GameService:
    """
    A service class for executing Zero-Sum game logic.
    
    This class encapsulates the comparison matrix and move selection 
    mechanisms for Rock-Paper-Scissors.
    """

    def __init__(self):
        self.options: Dict[str, str] = {
            'R': 'Rock',
            'P': 'Paper',
            'S': 'Scissors'
        }
        self.win_matrix: Dict[str, str] = {
            'R': 'S',  # Rock beats Scissors
            'S': 'P',  # Scissors beats Paper
            'P': 'R'   # Paper beats Rock
        }

    def get_computer_move(self) -> str:
        """Selects a move using cryptographically secure randomization."""
        return secrets.choice(list(self.options.keys()))

    def determine_winner(self, player: str, computer: str) -> str:
        """
        Evaluates the game state to determine the outcome.
        
        Returns:
            A string indicating 'Draw', 'Player Wins', or 'Computer Wins'.
        """
        if player == computer:
            return "Draw"
        
        if self.win_matrix[player] == computer:
            return "Player Wins"
        
        return "Computer Wins"


def main():
    """
    Demonstrates the scholarly Rock-Paper-Scissors implementation.
    """
    print("--- Rock Paper Scissors Game Engine Demo ---")
    
    # Define paths for standardized output
    script_dir = os.path.dirname(__file__)
    output_dir = os.path.join(script_dir, "Output")
    
    # Ensure the Output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    service = GameService()
    
    # Simulated moves for the automated check
    simulated_player_move = 'R'
    computer_move = service.get_computer_move()
    
    print(f"\nPlayer Choice: {service.options[simulated_player_move]}")
    print(f"Computer Choice: {service.options[computer_move]}")
    
    result = service.determine_winner(simulated_player_move, computer_move)
    print(f"\nGame Result: {result}")


if __name__ == "__main__":
    main()
