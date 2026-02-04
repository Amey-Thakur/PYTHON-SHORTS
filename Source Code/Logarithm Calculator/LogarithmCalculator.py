"""
File: LogarithmCalculator.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A high-fidelity computational utility for logarithmic functions. This module 
    supports Natural Logarithms (ln), Common Logarithms (log10), and arbitrary 
    base logarithms using the Change of Base Formula.

Mathematical Logic:
    For any positive base b and value x, the logarithm is the inverse function 
     of exponentiation: b^y = x <=> log_b(x) = y.
    The Change of Base identity is utilized for arbitrary bases:
    log_b(x) = ln(x) / ln(b)
"""

import math
from typing import Optional

class LogarithmCalculator:
    """Scholarly implementation of logarithmic computation services."""
    
    @staticmethod
    def calculate(x: float, base: Optional[float] = None) -> float:
        """
        Computes the logarithm of x to the specified base.

        Args:
            x (float): The value to calculate the logarithm for (x > 0).
            base (Optional[float]): The logarithmic base (base > 0, base != 1). 
                                   Defaults to e (Natural Logarithm).

        Returns:
            float: The computed logarithmic value.

        Raises:
            ValueError: If x or base do not satisfy logarithmic domain constraints.
        """
        if x <= 0:
            raise ValueError("Mathematical error: Logarithm domain is (0, inf). Provided x <= 0.")
        
        if base is not None:
            if base <= 0 or base == 1:
                raise ValueError("Mathematical error: Logarithmic base must be > 0 and != 1.")
            return math.log(x, base)
        
        return math.log(x)

def run_calculation_demo():
    """Execution demo with diverse logarithmic test vectors."""
    print("--- Python Shorts: Logarithm Computational Service ---")
    
    calculator = LogarithmCalculator()
    
    test_cases = [
        (14, None),     # Natural Log (ln)
        (100, 10),     # Common Log (log10)
        (8, 2),        # Binary Log (log2)
        (2.71828, None), # ln(e)
        (10, 3)        # Arbitrary base
    ]

    for x, b in test_cases:
        try:
            result = calculator.calculate(x, b)
            base_str = "e" if b is None else str(b)
            print(f"[Input]: log_{base_str}({x})")
            print(f" -> Result: {result:.6f}\n")
        except Exception as e:
            print(f"[Error]: {e}")

if __name__ == "__main__":
    run_calculation_demo()