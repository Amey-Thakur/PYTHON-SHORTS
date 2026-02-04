"""
File: Password_Guesser.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A computational demonstration of brute-force combinatorial search logic. 
    This module simulates a password guessing engine that iteratively attempts 
    to match a target string through randomized sampling of the search space.

Mathematical Logic:
    Given a target string T of length L and an alphabet set A of size |A|, 
    the total search space S is defined by the combinatorial product:
    S = |A|^L
    The probability of finding the target in a single randomized attempt is:
    P = 1 / |A|^L
"""

import random
import string
import time
from typing import Tuple

class PasswordBruteForcer:
    """Scholarly implementation of combinatorial search and matching logic."""

    ALPHABET = string.ascii_lowercase

    @staticmethod
    def brute_force(target: str, delay: float = 0.0) -> Tuple[int, float]:
        """
        Attempts to guess the target string through randomized iteration.

        Args:
            target (str): The target password to match.
            delay (float): Optional delay between attempts for visualization.

        Returns:
            Tuple[int, float]: The total attempts made and the elapsed time.
        """
        target = target.lower()
        target_len = len(target)
        guess = ""
        attempts = 0
        start_time = time.time()

        print(f"--- Initialization: Search Space = {len(PasswordBruteForcer.ALPHABET)}^{target_len} ---")

        while guess != target:
            attempts += 1
            # Generate a randomized sequence of the same length
            guess = "".join(random.choice(PasswordBruteForcer.ALPHABET) for _ in range(target_len))
            
            # Print periodic progress to avoid terminal flood for long searches
            if attempts % 1000 == 0:
                print(f"[Attempt {attempts}]: Current Guess: '{guess}'")
            
            if delay > 0:
                time.sleep(delay)

        end_time = time.time()
        duration = end_time - start_time
        
        return attempts, duration

def run_brute_force_demo():
    """Execution demo showcasing combinatorial search and successful matching."""
    print("--- Python Shorts: Password Guesser (Brute-Force Service) ---")
    
    # Using a short target to ensure timely execution in demo
    target_password = "cat"
    print(f"[Target]: '{target_password}'")
    
    attempts, duration = PasswordBruteForcer.brute_force(target_password)
    
    print("\n--- Successful Match Identified ---")
    print(f"Target Password: {target_password}")
    print(f"Total Attempts:  {attempts}")
    print(f"Execution Time:  {duration:.4f} seconds")

if __name__ == "__main__":
    run_brute_force_demo()