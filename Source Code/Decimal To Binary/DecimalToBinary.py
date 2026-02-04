"""
File: DecimalToBinary.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A scholarly implementation of a positional notation converter. This utility 
    transforms decimal integers (base-10) into their equivalent binary 
    representation (base-2) using the repeated division-remainder algorithm.

Mathematical Logic:
    Given a decimal integer N, its binary representation B = (b_k b_{k-1} ... b_0)_2 
    is found by solving:
    N = Σ_{i=0}^{k} b_i * 2^i
    where b_i ∈ {0, 1}. The algorithm uses b_i = (N // 2^i) % 2.
"""

from typing import List

class ConversionError(Exception):
    """Exception raised for invalid input during base conversion."""
    pass

def decimal_to_binary(n: int) -> str:
    """
    Converts a non-negative decimal integer to a base-2 binary string.
    
    Args:
        n (int): The decimal integer to convert.

    Returns:
        str: The binary string representation.

    Raises:
        ConversionError: If the input is not a non-negative integer.
    """
    if not isinstance(n, int) or n < 0:
        raise ConversionError("Input must be a non-negative integer.")
        
    if n == 0:
        return "0"
        
    bits: List[str] = []
    # O(log N) time complexity
    temp_n = n
    while temp_n > 0:
        bits.append(str(temp_n % 2))
        temp_n //= 2
        
    return "".join(reversed(bits))

def run_conversion_demo():
    """Execution demo with scholarly test vectors."""
    print("--- Python Shorts: Radis-2 Conversion (Decimal to Binary) ---")
    
    test_vectors = [0, 7, 10, 255, 1024, -5, "10"]
    
    for vector in test_vectors:
        try:
            result = decimal_to_binary(vector)
            print(f"[Input]: {str(vector):<5} | [Binary]: {result}")
        except ConversionError as e:
            print(f"[Input]: {str(vector):<5} | [Error]: {e}")

if __name__ == "__main__":
    run_conversion_demo()
