"""
File: ReverseWords.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module provides a scholarly interface for word-level string reversal.
    It preserves the internal character order of individual tokens while 
    inverting the global sequence of words using linear permutation paradigms.

Complexity Analysis:
    - Time Complexity: O(n), where n is the number of characters in the string.
    - Space Complexity: O(n) to store the intermediate list of tokens.

Logic:
    1. Tokenize the input string using whitespace as the primary delimiter.
    2. Perform a linear-time inversion of the resulting word list using indexing.
    3. Reconstruct the sentence by joining the inverted tokens with standardized 
       single-space delimiters.
    4. Handle boundary cases such as empty strings or single-word inputs gracefully.
"""

import os
from typing import List


class WordReversalService:
    """
    A service class for word-reversal operations.
    
    This class encapsulates the logic for string tokenization and 
    structural permutation of word sequences.
    """

    @staticmethod
    def reverse_word_sequence(content: str) -> str:
        """
        Reverses the semantic order of words in a string.
        
        Args:
            content: The input string containing space-delimited words.
            
        Returns:
            A new string where the sequence of words is inverted.
            
        Complexity:
            Time Complexity: O(n), where n is the number of characters in the string.
            Space Complexity: O(n) to store the intermediate list of tokens.
        """
        if not content:
            return ""

        # Tokenization via whitespace delimiter
        tokens: List[str] = content.split()
        
        # Word-level inversion via list slicing (O(n) permutation)
        reversed_tokens: List[str] = tokens[::-1]
        
        # Reconstruction of the inverted string
        return " ".join(reversed_tokens)


def main():
    """
    Demonstrates the scholarly word reversal implementation.
    """
    print("--- Word Reversal Service Demo ---")
    
    # Define paths for standardized output
    script_dir = os.path.dirname(__file__)
    output_dir = os.path.join(script_dir, "Output")
    
    # Ensure the Output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        service = WordReversalService()
        
        # Demonstration input string containing repository metadata
        input_text = "Repository: PYTHON-SHORTS | Authors: Amey Thakur & Mega Satish"
            
        transformed_text = service.reverse_word_sequence(input_text)
        
        print("\nOriginal Content:")
        print(f"[{input_text}]")
        
        print("\nReversed Sequence:")
        print(f"[{transformed_text}]")
        
    except Exception as e:
        print(f"Execution Failure: {e}")


if __name__ == "__main__":
    main()
