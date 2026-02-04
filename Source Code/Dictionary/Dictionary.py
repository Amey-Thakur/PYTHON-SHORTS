"""
File: Dictionary.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    An advanced encapsulated WordDictionary service designed for lexical 
    analysis. This module implements a robust interface for word lookup, 
    simulating realistic I/O latency to model network-dependent or 
    disk-bound dictionary services.

Mathematical Foundation:
    The service is modeled as a hash mapping function f: K -> V, where K 
    is the set of lexical keys (strings) and V is the set of semantic 
    definitions (objects). Complexity is O(1) for retrieval in the average case.
"""

import time
from typing import Dict, List, Any, Optional, Union

class WordDictionaryError(Exception):
    """Custom exception for dictionary service failures."""
    pass

class WordDictionary:
    """An encapsulated lexical analysis service with simulated I/O overhead."""
    
    def __init__(self):
        # Initializing core knowledge base with diverse lexical entries
        self._data: Dict[str, Dict[str, Any]] = {
            "Success": {
                "definitions": ["The accomplishment of an aim or purpose.", "The attainment of popularity or profit."],
                "synonyms": ["Achievement", "Triumph", "Prosperity"]
            },
            "Algorithm": {
                "definitions": ["A process or set of rules to be followed in calculations or problem-solving.", "A finite sequence of rigorous instructions."]
            },
            "Python": {
                "definitions": [
                    "A large heavy-bodied non-venomous snake.",
                    "A high-level general-purpose programming language."
                ],
                "parts_of_speech": ["Noun", "Proper Noun"]
            }
        }

    def lookup(self, word: str) -> Dict[str, Any]:
        """
        Retrieves lexical metadata for a given word.
        
        Args:
            word (str): The term to analyze.
            
        Returns:
            Dict[str, Any]: Highly structured lexical data.
            
        Raises:
            WordDictionaryError: For invalid input or missing entries.
        """
        # Validate input sanitization (TC-04)
        if not word or not isinstance(word, str):
            raise WordDictionaryError("Invalid input: Argument must be a non-empty string.")

        # Simulate I/O Latency (Benchmark: ~2.2s per word)
        time.sleep(2.2)

        # Standard word lookup (TC-01, TC-02, TC-05)
        # Case insensitive lookup
        normalized_word = word.strip().capitalize()
        entry = self._data.get(normalized_word)

        if not entry:
            # Graceful failure for missing entries (TC-03)
            raise WordDictionaryError(f"Word not found: '{word}' is not in the knowledge base.")

        return entry

def run_lexical_demo():
    """Execution demo following user-specified validation scenarios."""
    print("--- Python Shorts: Advanced Lexical Analysis (Dictionary) ---")
    service = WordDictionary()
    
    test_cases = ["Success", "Algorithm", "NonExistent", "", "Python"]
    
    for word in test_cases:
        print(f"\n[Requesting Lookup]: '{word}'")
        start_time = time.time()
        try:
            result = service.lookup(word)
            latency = time.time() - start_time
            print(f"[Status]: Success | [Latency]: {latency:.2f}s")
            print(f"[Payload]: {result}")
        except WordDictionaryError as e:
            latency = time.time() - start_time
            print(f"[Status]: Error   | [Latency]: {latency:.2f}s")
            print(f"[Description]: {e}")

if __name__ == "__main__":
    run_lexical_demo()