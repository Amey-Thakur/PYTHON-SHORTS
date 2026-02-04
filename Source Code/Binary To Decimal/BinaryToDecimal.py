"""
File: BinaryToDecimal.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This utility converts binary strings (base-2) into decimal integers (base-10).
    The algorithm processes the binary string from right to left, summing
    the powers of 2 for each '1' bit encountered.

Complexity Analysis:
    - Time Complexity: O(N), where N is the length of the binary string.
    - Space Complexity: O(1) iterative processing.

Logic:
    1. Validate that the input string contains only '0' and '1' characters.
    2. Iterate through the string in reverse.
    3. Maintain a multiplier for each position (1, 2, 4, 8...).
    4. Accumulate the total if the current character is '1'.
    5. Return the decimal result.
"""

class BinaryToDecimalError(Exception):
    """Custom exception for Binary conversion errors."""
    pass

def binary_to_decimal(binary_str: str) -> int:
    """
    Converts a binary string to its decimal integer equivalent.

    Args:
        binary_str (str): A string consisting only of '0's and '1's.

    Returns:
        int: The base-10 integer value.

    Raises:
        BinaryToDecimalError: If input is not a string or contains invalid characters.
    """
    if not isinstance(binary_str, str):
        raise BinaryToDecimalError("Input must be a string.")
    
    if not all(char in '01' for char in binary_str):
        raise BinaryToDecimalError("Invalid binary string: Must only contain 0 and 1.")

    decimal_val = 0
    # Process from right to left using powers of 2
    for i, digit in enumerate(reversed(binary_str)):
        if digit == '1':
            decimal_val += 2 ** i
            
    return decimal_val

def run_conversion_demo() -> None:
    """Demonstrates binary to decimal conversion."""
    print("--- Python Shorts: Binary to Decimal Converter ---")
    inputs = ["1010", "1111", "100", "0"]
    for b in inputs:
        try:
            print(f"Binary: {b:>5} | Decimal: {binary_to_decimal(b)}")
        except BinaryToDecimalError as e:
            print(f"Error for {b}: {e}")

if __name__ == '__main__':
    run_conversion_demo()
