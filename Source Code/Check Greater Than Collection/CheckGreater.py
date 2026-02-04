"""
File: CheckGreater.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This utility verifies if all elements in a numeric collection (Iterable)
    strictly exceed a specified threshold. It implements the universal 
    quantification (∀) predicate logic.

Mathematical Logic:
    ∀ x ∈ C, x > τ
    Where C is the collection and τ is the threshold.
"""

from typing import Iterable, Union

def is_all_greater(collection: Iterable[Union[int, float]], threshold: Union[int, float]) -> bool:
    """
    Verifies if every element in the collection is strictly greater than the threshold.
    
    Args:
        collection (Iterable): List, tuple, or other iterable of numbers.
        threshold (Numeric): The value against which all elements are compared.

    Returns:
        bool: True if every element > threshold, otherwise False.
    """
    # Universal quantification via early-exit search for counter-example
    for item in collection:
        if item <= threshold:
            return False
    return True

def run_demo():
    """Execution demo with multiple test scenarios."""
    test_cases = [
        {"data": [10, 20, 30], "threshold": 5, "label": "Positive Case"},
        {"data": [10, 2, 30], "threshold": 5, "label": "Negative Case (contains 2)"},
        {"data": [], "threshold": 5, "label": "Empty Collection (Vacuous Truth)"},
        {"data": [5, 5, 5], "threshold": 5, "label": "Equality Case (Strict Greater Check)"}
    ]

    print("--- Python Shorts: Collection Range Validation ---")
    for case in test_cases:
        result = is_all_greater(case["data"], case["threshold"])
        print(f"[{case['label']}] Data: {case['data']}, Threshold: {case['threshold']} -> Result: {result}")

if __name__ == "__main__":
    run_demo()
