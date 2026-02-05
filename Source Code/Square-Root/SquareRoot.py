"""
File: SquareRoot.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements square root computation using the Newton-Raphson 
    iterative approximation method. It demonstrates classical numerical analysis 
    techniques for finding roots of equations, converging quadratically to the 
    true value with high precision.

Complexity Analysis:
    - Time Complexity: O(log n) iterations to reach desired precision.
    - Space Complexity: O(1) auxiliary space.

Logic:
    1. Start with an initial guess x₀ (often n/2 or 1).
    2. Apply the Newton-Raphson iteration: x_{k+1} = (x_k + n/x_k) / 2
    3. Repeat until |x_{k+1} - x_k| < ε (convergence threshold).
    4. Return the final approximation as the square root.
"""

from typing import Optional


class SquareRootService:
    """
    A service class for computing square roots via numerical approximation.
    """

    def __init__(self, epsilon: float = 1e-10, max_iterations: int = 100):
        """
        Initializes the service with convergence parameters.
        
        Args:
            epsilon: Convergence threshold (tolerance).
            max_iterations: Maximum number of iterations to prevent infinite loops.
        """
        self.epsilon = epsilon
        self.max_iterations = max_iterations

    def newton_raphson(self, n: float) -> Optional[float]:
        """
        Computes the square root using the Newton-Raphson method.
        
        Args:
            n: The number to find the square root of.
            
        Returns:
            The approximate square root, or None if n is negative.
        """
        if n < 0:
            print("Error: Cannot compute square root of negative number.")
            return None
        
        if n == 0:
            return 0.0

        # Initial guess
        x = n / 2.0
        
        for iteration in range(self.max_iterations):
            # Newton-Raphson formula: x_new = (x + n/x) / 2
            x_new = (x + n / x) / 2.0
            
            # Check for convergence
            if abs(x_new - x) < self.epsilon:
                return x_new
            
            x = x_new
        
        # Return best approximation if max iterations reached
        return x

    def compute(self, n: float) -> Optional[float]:
        """
        Public interface for square root computation.
        
        Args:
            n: The number to find the square root of.
            
        Returns:
            The square root approximation.
        """
        result = self.newton_raphson(n)
        return result


def main():
    """
    Demonstrates the scholarly Square Root implementation.
    """
    print("--- Square Root Service Demo ---")
    
    try:
        num_str = input("Enter a number: ")
        num = float(num_str)
    except ValueError:
        print("Invalid input. Using default value 25.0")
        num = 25.0

    service = SquareRootService(epsilon=1e-10)
    result = service.compute(num)
    
    if result is not None:
        print(f"The square root of {num:.3f} is {result:.10f}")
        print(f"Verification: {result:.10f}² = {result**2:.10f}")
    
    print("\nComputation Complete.")


if __name__ == "__main__":
    main()
