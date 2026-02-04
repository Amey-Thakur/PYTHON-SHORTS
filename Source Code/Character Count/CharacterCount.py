"""
File: CharacterCount.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This script performs professional lexical analysis on a string, 
    calculating the frequency of each character (including whitespace and symbols).
    It returns a sorted frequency map for easy analysis.

Complexity Analysis:
    - Time Complexity: O(N), where N is the length of the string.
    - Space Complexity: O(U), where U is the number of unique characters.

Logic:
    1. Validate that the input is a string.
    2. Use `collections.Counter` for efficient O(N) frequency counting.
    3. Sort the resulting map by character for consistent output.
    4. Provide a filtered view option (e.g., ignoring whitespace).
"""

from collections import Counter
from typing import Dict, Any

def count_characters(text: str, ignore_whitespace: bool = False) -> Dict[str, int]:
    """
    Generates a frequency map for characters in a given string.

    Args:
        text (str): The input string to analyze.
        ignore_whitespace (bool): If True, spaces/tabs will be excluded.

    Returns:
        Dict[str, int]: A sorted dictionary of character counts.

    Raises:
        TypeError: If input text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected string, got {type(text).__name__}")

    if ignore_whitespace:
        text = "".join(text.split())

    counts = Counter(text)
    # Return as a dictionary sorted by character key
    return dict(sorted(counts.items()))

def run_count_demo() -> None:
    """Demonstrates character frequency analysis."""
    print("--- Python Shorts: Character Frequency Analysis ---")
    sample = "Scholarly Research 2022"
    results = count_characters(sample)
    print(f"Sample: '{sample}'")
    for char, count in results.items():
        char_repr = f"'{char}'" if char != " " else "'space'"
        print(f"  {char_repr:<8}: {count}")

if __name__ == '__main__':
    run_count_demo()
