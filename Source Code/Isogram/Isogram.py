"""
File: Isogram.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A high-fidelity implementation of an Isogram verifier. This module leverages 
    Set Theory to determine character uniqueness within a lexical string, 
    identifying "non-pattern words" (isograms) where each character appears 
    at most once.

Mathematical Logic:
    Let S be the set of characters in a string. The string is an isogram if and only 
    if the cardinality of S is equal to the length of the string after ignoring 
    non-alphabetic characters. Formally, |S| = length(string) implies an 
    injective mapping from positions to characters.
"""

from typing import List

class IsogramVerifier:
    """Scholarly implementation of an Isogram verification service."""
    
    @staticmethod
    def verify(text: str) -> bool:
        """
        Determines whether the provided string is an isogram.

        Args:
            text (str): The lexical string to evaluate.

        Returns:
            bool: True if the string is an isogram (no repeating characters), 
                  False otherwise.
        """
        # Normalization: lower case and filtering for alphabetic transparency
        clean_text = [char.lower() for char in text if char.isalpha()]
        
        # Uniqueness Test using Hash-Set Cardinality
        unique_chars = set(clean_text)
        
        return len(unique_chars) == len(clean_text)

def run_isogram_demo():
    """Execution demo with diverse logological test vectors."""
    print("--- Python Shorts: Isogram Verification & Set Cardinality ---")
    
    test_vectors = [
        "isogram",
        "eleven",
        "subdermatoglyphic",
        "Alphabet",
        "thumbscrew-japingly",
        "Hjelmqvist-Gryb-Zock-Pfund-Wax",
        "Emily Jung Schwartzkopf",
        "accentor",
        ""
    ]

    for word in test_vectors:
        result = IsogramVerifier.verify(word)
        status = "PASSED (Isogram)" if result else "FAILED (Repeating Characters)"
        print(f"[Input]: '{word}'")
        print(f" -> Result: {status}\n")

if __name__ == "__main__":
    run_isogram_demo()
