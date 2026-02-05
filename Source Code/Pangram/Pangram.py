r"""
File: Pangram.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A high-fidelity computational utility for verifying pangrams. A pangram is 
    a sentence containing every letter of the alphabet at least once. This 
    module utilizes set cardinality to achieve O(n) verification efficiency.

Mathematical Logic:
    Let A be the set of all unique alphabetic characters in a given string S. 
    Let L be the set of all letters in the English alphabet (a-z). 
    S is a pangram if and only if L is a subset of A, which implies |A \cap L| = 26.
"""

import string

class PangramVerifier:
    """Scholarly implementation of alphabetic coverage verification."""
    
    ALPHABET_SET = set(string.ascii_lowercase)
    ALPHABET_COUNT = 26

    @staticmethod
    def is_pangram(sentence: str) -> bool:
        """
        Determines if the provided sentence is a pangram.

        Args:
            sentence (str): The input string to verify.

        Returns:
            bool: True if every letter of the alphabet is present, False otherwise.
        """
        # Normalize: Filter non-alphabetic characters and convert to lowercase
        # Then convert to a set to find unique characters
        found_chars = {char.lower() for char in sentence if char.isalpha()}
        
        # Check if the cardinality of the intersection with the alphabet is 26
        return len(found_chars) == PangramVerifier.ALPHABET_COUNT

def run_pangram_demo():
    """Execution demo showcasing alphabetic coverage across diverse vectors."""
    print("--- Python Shorts: Pangram Verification Service ---")
    
    test_vectors = [
        "The quick brown fox jumps over the lazy dog",
        "Pack my box with five dozen liquor jugs",
        "The quick brown fox jumped over the lazy dog",  # Missing 's'
        "Five quacking Zephyrs jolt my wax bed",
        "Hello World",
        "123!@#",
        ""
    ]

    for vector in test_vectors:
        result = PangramVerifier.is_pangram(vector)
        status = "is a Pangram" if result else "is NOT a Pangram"
        print(f"[Input]:  \"{vector}\"")
        print(f" -> Status: {status}\n")

if __name__ == "__main__":
    run_pangram_demo()
