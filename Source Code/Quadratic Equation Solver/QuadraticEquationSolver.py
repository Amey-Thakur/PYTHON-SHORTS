"""
File: QuadraticEquationSolver.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    A computational service for solving quadratic equations of the form 
    ax^2 + bx + c = 0. This module calculates roots in both real and 
    complex domains using the quadratic formula and discriminant analysis.

Mathematical Logic:
    For a quadratic equation with coefficients a, b, and c, the roots 
    are determined by the formula:
    x = (-b +/- sqrt(b^2 - 4ac)) / (2a)
    The expression (b^2 - 4ac) is the discriminant (D), which 
    characterizes the nature of the roots.
"""

import cmath
from typing import Tuple, Union

class QuadraticSolver:
    """Scholarly implementation of quadratic root calculation services."""

    @staticmethod
    def solve(a: float, b: float, c: float) -> Tuple[complex, complex]:
        """
        Calculates the roots of a quadratic equation ax^2 + bx + c = 0.

        Args:
            a (float): Coefficient of x^2.
            b (float): Coefficient of x.
            c (float): Constant term.

        Returns:
            Tuple[complex, complex]: The two roots of the equation.

        Raises:
            ValueError: If the coefficient 'a' is zero (equation is not quadratic).
        """
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation.")

        # Calculate the discriminant D = b^2 - 4ac
        discriminant = (b**2) - (4*a*c)

        # Utilize cmath.sqrt for seamless support of complex roots
        root_d = cmath.sqrt(discriminant)
        
        sol1 = (-b - root_d) / (2 * a)
        sol2 = (-b + root_d) / (2 * a)

        return sol1, sol2

def run_solver_demo():
    """Execution demo showcasing root classification and calculation."""
    print("--- Python Shorts: Quadratic Equation Solver Service ---")
    
    # Test cases representing different discriminant states
    test_cases = [
        {"a": 1, "b": 5, "c": 6, "desc": "Two Real Roots (D > 0)"},
        {"a": 1, "b": 2, "c": 1, "desc": "One Real Root (D = 0)"},
        {"a": 1, "b": 0, "c": 1, "desc": "Complex Roots (D < 0)"}
    ]

    solver = QuadraticSolver()

    for case in test_cases:
        a, b, c = case["a"], case["b"], case["c"]
        print(f"\n[Case]: {case['desc']}")
        print(f"Equation: {a}x^2 + {b}x + {c} = 0")
        
        try:
            r1, r2 = solver.solve(a, b, c)
            print(f" -> Root 1: {r1}")
            print(f" -> Root 2: {r2}")
        except ValueError as e:
            print(f" -> Error: {e}")

if __name__ == "__main__":
    run_solver_demo()