"""
File: Palindrome.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A computational utility for verifying palindromic symmetry in strings. 
    This module implements an optimized two-pointer approach to achieve 
    O(n) time complexity with O(1) auxiliary space.

Mathematical Logic:
    A string S of length n is a palindrome if it remains invariant under 
    the reversal operation: S = S^R.
    Formally, for all integers i in [0, n-1]: S[i] = S[n-1-i].
"""

import re

class PalindromeVerifier:
    """Scholarly implementation of palindromic symmetry verification."""
    
    @staticmethod
    def is_palindrome(text: str, ignore_non_alphanumeric: bool = True) -> bool:
        """
        Determines if the provided string is a palindrome.

        Args:
            text (str): The input string to verify.
            ignore_non_alphanumeric (bool): Whether to skip spaces and symbols.

        Returns:
            bool: True if the string is symmetrical, False otherwise.
        """
        if ignore_non_alphanumeric:
            # Normalize: lowercase and remove non-alphanumeric characters
            clean_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
        else:
            clean_text = text

        if not clean_text:
            return True

        # Optimized Two-Pointer Approach
        left, right = 0, len(clean_text) - 1
        while left < right:
            if clean_text[left] != clean_text[right]:
                return False
            left += 1
            right -= 1
            
        return True

def run_palindrome_demo():
    """Execution demo showcasing symmetry verification across diverse vectors."""
    print("--- Python Shorts: Palindrome Verification Service ---")
    
    test_cases = [
        "A man, a plan, a canal: Panama",
        "racecar",
        "hello",
        "Was it a car or a cat I saw?",
        "No 'x' in Nixon",
        "12321",
        "123456"
    ]

    for case in test_cases:
        result = PalindromeVerifier.is_palindrome(case)
        status = "is a Palindrome" if result else "is NOT a Palindrome"
        print(f"[Input]:  \"{case}\"")
        print(f" -> Status: {status}\n")

if __name__ == "__main__":
    run_palindrome_demo()
