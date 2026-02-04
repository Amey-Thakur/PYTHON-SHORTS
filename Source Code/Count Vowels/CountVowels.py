"""
File: CountVowels.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A scholarly implementation of a vowel frequency analyzer. This utility 
    performs lexical analysis on strings to calculate the cardinality of 
    the intersection between the input set and the set of standard English 
    vowels.

Mathematical Foundation:
    Let S be the multiset of characters in the input string.
    Let V = {a, e, i, o, u} be the set of vowels.
    Vowel Count = Σ_{x ∈ S} [x.lower() ∈ V]
"""

from typing import Dict, Tuple

def count_vowels(text: str) -> Tuple[int, Dict[str, int]]:
    """
    Performs frequency analysis to count vowels in the provided text.
    
    Args:
        text (str): The string content to analyze.

    Returns:
        Tuple[int, Dict[str, int]]: 
            - total: Total number of vowels found.
            - frequencies: Mapping of each vowel to its occurrence count.
    """
    vowels = "aeiou"
    # O(1) space for fixed-size frequency map
    frequences = {v: 0 for v in vowels}
    total = 0
    
    # O(N) time complexity traversal
    for char in text.lower():
        if char in frequences:
            frequences[char] += 1
            total += 1
            
    return total, frequences

def run_demo():
    """Execution demo with scholarly test vectors."""
    print("--- Python Shorts: Lexical Analysis - Vowel Counting ---")
    
    test_vectors = [
        "Scholarly Research 2022",
        "Python is powerful!",
        "AEIOU and sometimes Y",
        "12345!@#$%"
    ]
    
    for vector in test_vectors:
        total, breakdown = count_vowels(vector)
        print(f"\n[Input]: \"{vector}\"")
        print(f"Total Vowels: {total}")
        print(f"Frequencies : {breakdown}")

if __name__ == "__main__":
    run_demo()
