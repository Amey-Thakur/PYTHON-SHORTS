"""
File: PascalTriangle.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A high-fidelity computational utility for generating Pascal's Triangle. 
    This module implements an iterative Dynamic Programming approach to 
    efficiently compute binomial coefficients for triangular matrices.

Mathematical Logic:
    Pascal's Triangle is a triangular array of binomial coefficients. The 
    value at the n-th row and k-th column is given by the formula:
    C(n, k) = n! / (k! * (n-k)!)
    The iterative construction follows Pascal's Identity:
    P(n, k) = P(n-1, k-1) + P(n-1, k)
"""

from typing import List

class PascalTriangleGenerator:
    """Scholarly implementation of Pascal's Triangle generation services."""

    @staticmethod
    def generate(rows: int) -> List[List[int]]:
        """
        Generates a Pascal's Triangle with the specified number of rows.

        Args:
            rows (int): The number of rows to generate.

        Returns:
            List[List[int]]: A list of lists representing the triangle.
        """
        if rows <= 0:
            return []

        triangle = [[1]]
        for i in range(1, rows):
            prev_row = triangle[-1]
            # Pascal's Identity: Sum of two adjacent elements in the previous row
            row = [1]
            for j in range(1, len(prev_row)):
                row.append(prev_row[j-1] + prev_row[j])
            row.append(1)
            triangle.append(row)
            
        return triangle

    @staticmethod
    def display(rows: int):
        """
        Displays the Pascal's Triangle in a formatted matrix.

        Args:
            rows (int): The number of rows to display.
        """
        triangle = PascalTriangleGenerator.generate(rows)
        # Calculate padding for alignment based on the largest value (center of the last row)
        max_val = triangle[-1][len(triangle[-1]) // 2]
        width = len(str(max_val)) + 1
        
        print(f"--- Pascal's Triangle Generator ({rows} Rows) ---")
        for i, row in enumerate(triangle):
            # Center the row for triangular aesthetic
            row_str = " ".join(f"{val:{width}}" for val in row)
            print(f"Row {i:2}: {row_str.center(width * rows)}")
        print("-" * 40)

def run_demo():
    """Execution demo showcasing combinatorial matrices."""
    generator = PascalTriangleGenerator()
    
    # Standard 7-row triangle
    generator.display(7)
    
    # Extended 10-row triangle
    generator.display(10)

if __name__ == "__main__":
    run_demo()
