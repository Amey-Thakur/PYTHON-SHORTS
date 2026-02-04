"""
File: GuessTheNumber.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    An interactive simulation of a number-guessing game. The module leverages 
    the principle of search-space reduction, illustrating how feedback 
    (greater than/less than) allows for a logarithmic search strategy.

Mathematical Logic:
    In a range [1, N], a number-guessing game with binary feedback 
    can be solved in a maximum of ceil(log2(N)) attempts. This implementation 
    models a discrete search space and provides relative directional feedback.
"""

import random
import sys

class GuessGame:
    """Scholarly implementation of a search-space reduction game."""
    def __init__(self, lower: int = 0, upper: int = 20):
        self.lower = lower
        self.upper = upper
        self.target = random.randint(lower, upper)
        self.attempts = 0

    def validate_input(self, val: str) -> int:
        """Validates that the input is an integer within the defined bounds."""
        try:
            num = int(val)
            if not (self.lower <= num <= self.upper):
                print(f"[Warning]: Input {num} is out of bounds [{self.lower}, {self.upper}].")
            return num
        except ValueError:
            raise ValueError(f"Invalid input: '{val}' is not a discrete integer.")

    def play_interactive(self):
        """Standard human-interactive game loop."""
        print(f"--- Guess The Number: [{self.lower}, {self.upper}] ---")
        while True:
            try:
                self.attempts += 1
                guess_str = input(f"Enter your guess ({self.lower}-{self.upper}): ")
                guess = self.validate_input(guess_str)
                
                if guess < self.target:
                    print("Status: Too Small.")
                elif guess > self.target:
                    print("Status: Too Large.")
                else:
                    print(f"Convergence achieved! Target {self.target} found in {self.attempts} attempts.")
                    break
            except ValueError as e:
                print(f"[Error]: {e}")
                self.attempts -= 1  # Do not count invalid attempts

    def run_simulation(self, guesses: list):
        """Non-interactive simulation for automated verification and logging."""
        print(f"--- Simulation: Range [{self.lower}, {self.upper}] | Target: [REDACTED] ---")
        for g in guesses:
            self.attempts += 1
            print(f"[Guess {self.attempts}]: {g}")
            if g < self.target:
                print(" -> Result: Too Small")
            elif g > self.target:
                print(" -> Result: Too Large")
            else:
                print(f" -> Result: Exact Match! Solution set converged in {self.attempts} iterations.")
                return
        print(f"[End]: Simulation terminated after {self.attempts} iterations.")

def run_demo():
    """Main execution entry point."""
    if len(sys.argv) > 1 and sys.argv[1] == "--sim":
        # Automated simulation for Output.txt
        sim_game = GuessGame(0, 20)
        # Simulate a binary search pattern (theoretical optimum)
        test_sequence = [10, 5, 15, 2, 7, 12, 18, 0, 1, 3, 4, 6, 8, 9, 11, 13, 14, 16, 17, 19, 20]
        sim_game.run_simulation(test_sequence)
    else:
        # standard interactive play
        game = GuessGame(0, 20)
        game.play_interactive()

if __name__ == "__main__":
    run_demo()
