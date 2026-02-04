"""
File: HangmanGame.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A high-fidelity implementation of the Hangman word-guessing game. This module 
    leverages Set Theory for character state management and provides a robust 
    engine for interactive and simulated gameplay.

Mathematical Logic:
    Let W be the set of characters in the target word and G be the set of 
    guessed characters. The game state is defined by the intersection G ∩ W. 
    Convergence is achieved when (G ∩ W) = W.
"""

import random
import sys
from typing import Set, List

class HangmanEngine:
    """Scholarly implementation of a set-based word-guessing engine."""
    def __init__(self, vocabulary: List[str]):
        self.word = random.choice(vocabulary).lower()
        self.word_chars: Set[str] = set(self.word)
        self.guesses: Set[str] = set()
        self.max_chances = len(self.word) + 2
        self.remaining_chances = self.max_chances

    def process_guess(self, char: str) -> bool:
        """Processes a single character guess."""
        char = char.lower()
        if char in self.guesses:
            print(f"[Warning]: '{char}' has already been evaluated.")
            return False
            
        self.guesses.add(char)
        if char in self.word_chars:
            print(f"Status: Intersection updated. '{char}' is present.")
            return True
        else:
            self.remaining_chances -= 1
            print(f"Status: Null intersection. '{char}' is absent. Chances left: {self.remaining_chances}")
            return False

    def get_display_word(self) -> str:
        """Returns the current state of the word with hidden placeholders."""
        return " ".join([char if char in self.guesses else "_" for char in self.word])

    def is_solved(self) -> bool:
        """Checks if the guess set covers the target word character set."""
        return self.word_chars.issubset(self.guesses)

    def play_interactive(self):
        """Interactive loop for human players."""
        print("--- Hangman: Fruit Identification Protocol ---")
        while self.remaining_chances > 0:
            print(f"\nWord: {self.get_display_word()}")
            guess = input("Enter character guess: ").strip()
            
            if not guess.isalpha() or len(guess) != 1:
                print("[Error]: Input must be a single alphabetic character.")
                continue
                
            self.process_guess(guess)
            
            if self.is_solved():
                print(f"\nConvergence achieved! Word: {self.word}")
                print("Congratulations, the lexical state matches the target.")
                return

        print(f"\nLexical termination reached. Target was: {self.word}")

    def run_simulation(self, test_guesses: List[str]):
        """Deterministic simulation for automated verification."""
        print(f"--- Simulation: Target Word [REDACTED] ---")
        for char in test_guesses:
            print(f"\n[Action]: Evaluating '{char}'")
            self.process_guess(char)
            print(f"[Current State]: {self.get_display_word()}")
            
            if self.is_solved():
                print(" -> Result: Convergence achieved! Target identified.")
                return
            if self.remaining_chances <= 0:
                print(" -> Result: Chance depletion. Search terminated.")
                return

def run_demo():
    """Main execution entry point."""
    fruits = [
        'apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 
        'pineapple', 'apricot', 'lemon', 'coconut', 'watermelon',
        'cherry', 'papaya', 'berry', 'peach', 'lychee', 'muskmelon'
    ]
    
    if len(sys.argv) > 1 and sys.argv[1] == "--sim":
        # Automated simulation for Output.txt
        engine = HangmanEngine(['pineapple'])
        # Logical test sequence for 'pineapple'
        test_sequence = ['a', 'e', 'i', 'p', 'x', 'n', 'l']
        engine.run_simulation(test_sequence)
    else:
        engine = HangmanEngine(fruits)
        engine.play_interactive()

if __name__ == "__main__":
    run_demo()
