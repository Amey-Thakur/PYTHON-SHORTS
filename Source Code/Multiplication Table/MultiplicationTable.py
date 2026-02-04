"""
File: MultiplicationTable.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A computational utility for generating arithmetic multiplication tables. 
    This module provides a structured approach to scalar multiplication, 
    representing products as an arithmetic progression series.

Mathematical Logic:
    For a given integer 'n' (the multiplicand) and a range [1, m], the 
    multiplication table consists of the sequence:
    {f(i) = n * i | i is an element of [1, m]}
    This represents an arithmetic progression with initial term n and 
    common difference n.
"""

from typing import List

class MultiplicationTableGenerator:
    """Scholarly implementation of multiplication table generation services."""
    
    @staticmethod
    def generate(multiplicand: int, limit: int = 10) -> List[int]:
        """
        Generates the product sequence for a given number.

        Args:
            multiplicand (int): The base number to multiply.
            limit (int): The upper bound of the multiplier (default is 10).

        Returns:
            List[int]: A list containing the product sequence.
        """
        return [multiplicand * i for i in range(1, limit + 1)]

    @staticmethod
    def display_grid(multiplicand: int, limit: int = 10):
        """
        Displays a formatted grid of the multiplication table.

        Args:
            multiplicand (int): The base number to multiply.
            limit (int): The upper bound of the multiplier.
        """
        print(f"--- Multiplication Table for {multiplicand} (1 to {limit}) ---")
        products = MultiplicationTableGenerator.generate(multiplicand, limit)
        
        for i, product in enumerate(products, 1):
            # Formatted alignment for structural clarity
            print(f"{multiplicand:2} x {i:2} = {product:3}")
        print("-" * 30)

def run_demo():
    """Execution demo showcasing arithmetic product matrices."""
    generator = MultiplicationTableGenerator()
    
    # Standard 1 to 10 table
    generator.display_grid(7)
    
    # Custom range table
    generator.display_grid(12, 12)

if __name__ == "__main__":
    run_demo()
