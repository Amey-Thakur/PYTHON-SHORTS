"""
File: Anagram.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    An anagram is a word or phrase formed by rearranging the letters of a 
    different word or phrase, typically using all the original letters 
    exactly once. This script provides a production-ready utility to 
    identify all valid anagrams of a target string from a collection of candidates.

Complexity Analysis:
    - Time Complexity: O(N * K), where N is the number of candidates 
      and K is the average length of the strings (due to character counting).
    - Space Complexity: O(K), required to store the frequency map of 
      the target word.

Logic:
    1. Validate inputs to ensure they meet expected types (strings and lists).
    2. Normalize the target word (lowercase) and generate its character frequency map.
    3. Iterate through the candidate list.
    4. For each candidate, verify it is not identical to the target (case-insensitive).
    5. Compare the candidate's frequency map with the target's map.
    6. Return the list of matching candidates.
"""

from collections import Counter
from typing import List, Optional

class AnagramError(Exception):
    """Custom exception for Anagram utility errors."""
    pass

def find_anagrams(target_word: str, candidate_list: List[str]) -> List[str]:
    """
    Identifies valid anagrams of a target word from a list of candidates.

    This function performs a case-insensitive search and ensures that the
    found anagram is not the exact same word as the target.

    Args:
        target_word (str): The primary word to find anagrams for.
        candidate_list (List[str]): A list of strings to search through.

    Returns:
        List[str]: A list of all strings from candidate_list that are anagrams of target_word.

    Raises:
        AnagramError: If target_word is not a string or candidate_list is not a list.
    """
    # Industry-standard type validation
    if not isinstance(target_word, str):
        raise AnagramError(f"Expected target_word to be 'str', got '{type(target_word).__name__}'")
    if not isinstance(candidate_list, list):
        raise AnagramError(f"Expected candidate_list to be 'list', got '{type(candidate_list).__name__}'")

    # Normalize target for case-insensitive processing and efficient frequency counting
    target_lower: str = target_word.lower()
    target_counts: Counter = Counter(target_lower)
    anagram_results: List[str] = []

    for candidate in candidate_list:
        # Input validation for candidates
        if not isinstance(candidate, str):
            continue
            
        candidate_lower: str = candidate.lower()

        # Performance Hint: Comparing lengths is O(1) before doing O(K) counting
        if len(target_lower) == len(candidate_lower) and target_lower != candidate_lower:
            if target_counts == Counter(candidate_lower):
                anagram_results.append(candidate)

    return anagram_results

def run_anagram_demo() -> None:
    """Executes a standard demonstration of the Anagram detection utility."""
    test_cases = [
        ("ant", ["tan", "stand", "at"]),
        ("master", ["stream", "pigeon", "maters"]),
        ("good", ["dog", "goody"]),
        ("allergy", ["gallery", "ballerina", "regally", "largely"]),
        ("BANANA", ["Banana"])
    ]

    print("--- Python Shorts: Anagram Detection Demo ---")
    for word, candidates in test_cases:
        try:
            results = find_anagrams(word, candidates)
            print(f"Target: {word:<10} | Found: {results}")
        except AnagramError as e:
            print(f"Error processing {word}: {e}")

if __name__ == '__main__':
    run_anagram_demo()
